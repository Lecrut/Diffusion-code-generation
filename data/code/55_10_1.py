def print_alphabet_triangle(height: int) -> None:
    for i in range(1, height + 1):
        row_chars = []
        for j in range(i):
            char_code = ord('A') + j
            row_chars.append(chr(char_code))
        print(' '.join(row_chars))

if __name__ == '__main__':
    print_alphabet_triangle(5)