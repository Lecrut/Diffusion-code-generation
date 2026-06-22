def generate_hollow_alphabet_triangle(base_width):
    if base_width <= 0:
        return ""
    
    lines = []
    for row in range(1, base_width + 1):
        line_chars = []
        for col in range(1, row + 1):
            if row == base_width or col == 1 or col == row:
                index = col - 1
                if index < 26:
                    char = chr(ord('A') + index)
                else:
                    char = chr(ord('A') + (index % 26))
                line_chars.append(char)
            else:
                line_chars.append(" ")
        lines.append(" ".join(line_chars))
    
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_hollow_alphabet_triangle(5)
    print(result)