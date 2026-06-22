def generate_hollow_alphabet_triangle(base_width):
    if base_width <= 0:
        return ""
    rows = []
    for i in range(base_width):
        row_chars = []
        for j in range(2 * base_width - 1):
            is_left_edge = j == base_width - 1 - i
            is_right_edge = j == base_width - 1 + i
            is_bottom = i == base_width - 1
            if is_left_edge or is_right_edge or is_bottom:
                char_index = j
                if char_index < 0:
                    char_index = 0
                if char_index >= 26:
                    char_index = char_index % 26
                char = chr(ord('A') + char_index)
                row_chars.append(char)
            else:
                row_chars.append(' ')
        rows.append("".join(row_chars))
    return "\n".join(rows)

if __name__ == '__main__':
    result = generate_hollow_alphabet_triangle(5)
    print(result)