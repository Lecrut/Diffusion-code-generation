def hollow_alphabet_triangle(base_width):
    if base_width <= 0:
        return ""
    result = []
    start_char = ord('A')
    for i in range(base_width):
        row_chars = []
        for j in range(base_width - i):
            char_code = start_char + i + j
            if char_code > ord('Z'):
                char_code = ord('A') + (char_code - ord('A')) % 26
            current_char = chr(char_code)
            if i == 0 or i == base_width - 1 or j == 0 or j == base_width - i - 1:
                row_chars.append(current_char)
            else:
                row_chars.append(' ')
        result.append("".join(row_chars))
    return "\n".join(result)

if __name__ == '__main__':
    sample_width = 5
    print(hollow_alphabet_triangle(sample_width))