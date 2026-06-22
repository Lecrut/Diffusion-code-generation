def generate_hollow_alphabet_triangle(base_width):
    if base_width < 1:
        return ""
    
    lines = []
    start_ord = ord('A')
    
    for i in range(base_width):
        row_chars = []
        for j in range(base_width):
            if i == 0 or i == base_width - 1 or j == 0 or j == i:
                char_code = start_ord + j
                if char_code > ord('Z'):
                    char_code = ord('A') + (char_code - ord('A') - 1) % 26
                row_chars.append(chr(char_code))
            else:
                row_chars.append(' ')
        lines.append(''.join(row_chars))
    
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_hollow_alphabet_triangle(5)
    print(result)