def print_triangular_alphabet(size: int) -> None:
    if size <= 0:
        return
    alphabet = [chr(ord('A') + i) for i in range(26)]
    current_line_length = 1
    current_char_index = 0
    for row in range(1, size + 1):
        line_chars = []
        for col in range(1, row + 1):
            line_chars.append(alphabet[current_char_index % 26])
            current_char_index += 1
        print(' '.join(line_chars))
if __name__ == '__main__':
    sample_size = 5
    print_triangular_alphabet(sample_size)