def generate_alphabet_triangle(rows: int) -> list:
    if rows <= 0:
        return []
    
    pattern = []
    current_char_code = 65
    
    for row_num in range(1, rows + 1):
        row_chars = []
        for _ in range(row_num):
            if current_char_code > 90:
                current_char_code = 65
            row_chars.append(chr(current_char_code))
            current_char_code += 1
        pattern.append("".join(row_chars))
    
    return pattern

if __name__ == '__main__':
    sample_rows = 7
    result = generate_alphabet_triangle(sample_rows)
    for line in result:
        print(line)