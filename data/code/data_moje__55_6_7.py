def hollow_alphabet_triangle(base_width):
    if base_width < 1:
        return ""
    lines = []
    for i in range(1, base_width + 1):
        char_index = i - 1
        char = chr(ord('A') + char_index % 26)
        if i == 1:
            line = char
        elif i == base_width:
            chars_needed = base_width
            line_chars = []
            for j in range(chars_needed):
                idx = j
                line_chars.append(chr(ord('A') + idx % 26))
            line = "".join(line_chars)
        else:
            left_char = chr(ord('A') + (i - 1) % 26)
            right_char = chr(ord('A') + (i - 1) % 26)
            spaces = ' ' * (2 * (i - 1) - 1)
            line = left_char + spaces + right_char
        padding = ' ' * (base_width - i)
        lines.append(padding + line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = hollow_alphabet_triangle(5)
    print(result)