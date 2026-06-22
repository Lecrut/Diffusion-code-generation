def print_alphabet_triangle(rows):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1, rows + 1):
        row_chars = []
        for j in range(i):
            if j < len(alphabet):
                row_chars.append(alphabet[j].upper())
            else:
                row_chars.append(alphabet[j % len(alphabet)].upper())
        print(" ".join(row_chars))

if __name__ == '__main__':
    sample_rows = 5
    print_alphabet_triangle(sample_rows)