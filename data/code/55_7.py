def reverse_alphabet_triangle(start_char: str, end_char: str) -> list:
    start_ord = ord(start_char.lower())
    end_ord = ord(end_char.lower())
    if start_ord <= end_ord:
        char_range = range(start_ord, end_ord + 1)
    else:
        char_range = range(start_ord, end_ord - 1, -1)
    char_sequence = [chr(code) for code in char_range]
    n = len(char_sequence)
    result = []
    current_idx = 0
    for row in range(1, n + 1):
        row_chars = char_sequence[current_idx:current_idx + row]
        if start_ord > end_ord:
            row_chars = row_chars[::-1]
        result.append(' '.join(row_chars))
        current_idx += row
        if current_idx >= n:
            break
    return result
if __name__ == '__main__':
    start = 'Z'
    end = 'A'
    result = reverse_alphabet_triangle(start, end)
    for line in result:
        print(line)