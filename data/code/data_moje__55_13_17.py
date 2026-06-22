def generate_triangular_alphabet_pattern(rows):
    import string
    alphabet = string.ascii_uppercase
    pattern = []
    for i in range(1, rows + 1):
        row_letters = []
        for j in range(i):
            letter_index = j % len(alphabet)
            row_letters.append(alphabet[letter_index])
        pattern.append(' '.join(row_letters))
    return pattern

def print_triangular_alphabet_pattern(rows):
    pattern = generate_triangular_alphabet_pattern(rows)
    for line in pattern:
        print(line)
if __name__ == '__main__':
    sample_rows = 5
    print_triangular_alphabet_pattern(sample_rows)