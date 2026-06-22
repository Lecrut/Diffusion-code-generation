def generate_hollow_alphabet_triangle(base_width):
    if base_width < 1:
        return ""
    
    lines = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(1, base_width + 1):
        row_chars = []
        for j in range(1, 2 * base_width):
            if i == 1:
                if j == base_width:
                    row_chars.append(alphabet[0])
                else:
                    row_chars.append(" ")
            elif i == base_width:
                if j % 2 == 0:
                    row_chars.append(" ")
                else:
                    char_index = (j - 1) // 2
                    if char_index < len(alphabet):
                        row_chars.append(alphabet[char_index])
                    else:
                        row_chars.append(alphabet[-1])
            else:
                left_pos = base_width - i + 1
                right_pos = base_width + i - 1
                if j == left_pos or j == right_pos:
                    char_index = i - 1
                    if char_index < len(alphabet):
                        row_chars.append(alphabet[char_index])
                    else:
                        row_chars.append(alphabet[-1])
                else:
                    row_chars.append(" ")
        
        line = "".join(row_chars)
        stripped_line = line.rstrip()
        lines.append(stripped_line)
    
    return "\n".join(lines)

if __name__ == '__main__':
    sample_width = 5
    result = generate_hollow_alphabet_triangle(sample_width)
    print(result)