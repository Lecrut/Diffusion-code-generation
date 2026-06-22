def print_left_aligned_alphabet_triangle():
    n = 5
    for i in range(1, n + 1):
        row_chars = []
        char_val = 65
        for j in range(i):
            row_chars.append(chr(char_val))
            char_val += 1
        print(''.join(row_chars))

if __name__ == '__main__':
    print_left_aligned_alphabet_triangle()