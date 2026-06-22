def generate_hollow_alphabet_triangle(base_width: int) -> list[str]:
    if base_width < 1:
        return []
    
    result = []
    max_char_code = ord('A') + 25
    current_char_code = ord('A')
    
    for i in range(base_width):
        row_chars = []
        for j in range(base_width - i):
            if j == 0:
                char_val = chr(ord('A') + i)
                row_chars.append(char_val)
            elif j == base_width - i - 1:
                if i == base_width - 1:
                    char_val = chr(ord('A') + i)
                else:
                    char_val = chr(ord('A') + i)
                row_chars.append(char_val)
            else:
                if i < 25:
                    char_val = chr(ord('A') + i)
                else:
                    char_val = 'Z'
                row_chars.append(char_val)
        
        row_str = "".join(row_chars)
        result.append(row_str)
    
    return result

if __name__ == '__main__':
    sample_base = 7
    triangle_lines = generate_hollow_alphabet_triangle(sample_base)
    for line in triangle_lines:
        print(line)