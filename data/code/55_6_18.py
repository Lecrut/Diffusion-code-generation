def generate_hollow_alphabet_triangle(base_width):
    if base_width <= 0:
        return ""
    lines = []
    start_ord = ord('A')
    for row in range(1, base_width + 1):
        row_chars = []
        for col in range(1, 2 * base_width):
            if row == 1:
                if col == base_width:
                    row_chars.append(chr(start_ord))
                else:
                    row_chars.append(' ')
            elif row == base_width:
                if col % 2 == 0:
                    row_chars.append(' ')
                else:
                    char_index = (col - 1) // 2
                    if char_index < base_width:
                        row_chars.append(chr(start_ord + char_index))
                    else:
                        row_chars.append(' ')
            else:
                left_pos = base_width - (row - 1)
                right_pos = base_width + (row - 1)
                if col == left_pos or col == right_pos:
                    char_index = (col - 1) // 2
                    if char_index < base_width:
                        row_chars.append(chr(start_ord + char_index))
                    else:
                        row_chars.append(' ')
                else:
                    row_chars.append(' ')
        line = "".join(row_chars).rstrip()
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_hollow_alphabet_triangle(5)
    print(result)