# DNA Sequence Analyzer
# This program analyzes a DNA sequence entered by the user.

def is_valid_dna(sequence):
    # Check if every letter is A, T, C, or G.
    for base in sequence:
        if base not in "ATCG":
            return False

    return True


def get_reverse_complement(sequence):
    # Create the matching DNA sequence.
    pairs = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    complement = ""

    for base in sequence:
        complement += pairs[base]

    # Reverse the complement before returning it.
    return complement[::-1]


def count_codons(sequence):
    # Count DNA groups that have 3 bases.
    codon_counts = {}

    # Ignore 1 or 2 leftover bases at the end.
    complete_length = len(sequence) - (len(sequence) % 3)

    for position in range(0, complete_length, 3):
        codon = sequence[position:position + 3]

        if codon not in codon_counts:
            codon_counts[codon] = 0

        codon_counts[codon] += 1

    return codon_counts


# Ask the user to enter a DNA sequence.
sequence = input("Enter a DNA sequence: ")

# Remove spaces and make letters uppercase.
sequence = sequence.replace(" ", "").upper()

# Check that the user entered something.
if sequence == "":
    print("You did not enter a DNA sequence.")

# Check that the sequence only has valid DNA bases.
elif is_valid_dna(sequence) == False:
    print("Invalid sequence. Please use only A, T, C, and G.")

else:
    # Count each DNA base.
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    c_count = sequence.count("C")
    g_count = sequence.count("G")

    # Calculate GC content.
    gc_content = ((g_count + c_count) / len(sequence)) * 100

    # Get reverse complement and codon counts.
    reverse_complement = get_reverse_complement(sequence)
    codon_counts = count_codons(sequence)

    # Display results on the screen.
    print()
    print("DNA Sequence Results")
    print("Sequence:", sequence)
    print("Length:", len(sequence))
    print("A count:", a_count)
    print("T count:", t_count)
    print("C count:", c_count)
    print("G count:", g_count)
    print("GC content:", round(gc_content, 2), "%")
    print("Reverse complement:", reverse_complement)

    print()
    print("Codon counts:")

    for codon in codon_counts:
        print(codon + ":", codon_counts[codon])

    # Save results in a text file.
    report_file = open("dna_report.txt", "w")

    report_file.write("DNA Sequence Results\n")
    report_file.write("Sequence: " + sequence + "\n")
    report_file.write("Length: " + str(len(sequence)) + "\n")
    report_file.write("A count: " + str(a_count) + "\n")
    report_file.write("T count: " + str(t_count) + "\n")
    report_file.write("C count: " + str(c_count) + "\n")
    report_file.write("G count: " + str(g_count) + "\n")
    report_file.write("GC content: " + str(round(gc_content, 2)) + "%\n")
    report_file.write("Reverse complement: " + reverse_complement + "\n")

    report_file.write("\nCodon counts:\n")

    for codon in codon_counts:
        report_file.write(codon + ": " + str(codon_counts[codon]) + "\n")

    report_file.close()

    print()
    print("Your results were saved in dna_report.txt")