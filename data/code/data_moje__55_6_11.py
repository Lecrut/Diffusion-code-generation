def generate_hollow_alphabet_triangle(base_width):
    if base_width < 1:
        return []
    
    result = []
    current_row = 1
    while current_row <= base_width:
        line_chars = []
        col = 1
        while col <= current_row:
            if col == 1 or col == current_row or current_row == base_width:
                char_code = 64 + col
                line_chars.append(chr(char_code))
            else:
                line_chars.append(" ")
            col += 1
        result.append("".join(line_chars))
        current_row += 1
    
    return result

if __name__ == '__main__':
    pattern = generate_hollow_alphabet_triangle(5)
    for line in pattern:
        print(line)