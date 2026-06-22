def generate_hollow_alphabet_triangle(base_width):
    if base_width <= 0:
        return ""
    
    result_lines = []
    for row in range(1, base_width + 1):
        line_chars = []
        for col in range(1, row + 1):
            if col == 1 or col == row or row == base_width:
                char = chr(ord('A') + row - 1)
                line_chars.append(char)
            else:
                line_chars.append(" ")
        line = "".join(line_chars)
        result_lines.append(line)
    
    return "\n".join(result_lines)

if __name__ == '__main__':
    print(generate_hollow_alphabet_triangle(6))