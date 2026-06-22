def generate_zigzag_alphabet_triangle(rows):
    if rows <= 0:
        return []
    
    pattern = []
    current_char_code = ord('A')
    direction = 1
    
    for r in range(1, rows + 1):
        row_chars = []
        for c in range(r):
            row_chars.append(chr(current_char_code))
            current_char_code += 1
            if current_char_code > ord('Z'):
                current_char_code = ord('A')
        
        if direction == 1:
            pattern.append(''.join(row_chars))
        else:
            pattern.append(''.join(reversed(row_chars)))
        
        direction *= -1
    
    return pattern

if __name__ == '__main__':
    sample_rows = 7
    result = generate_zigzag_alphabet_triangle(sample_rows)
    for line in result:
        print(line)