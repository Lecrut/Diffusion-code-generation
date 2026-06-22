def print_alphabet_triangle(rows):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(rows):
        if i >= len(alphabet):
            break
        row_chars = []
        for j in range(i + 1):
            if j < len(alphabet):
                row_chars.append(alphabet[j])
        print("".join(row_chars))

if __name__ == '__main__':
    sample_rows = 5
    print_alphabet_triangle(sample_rows)