def generate_zigzag_triangle(rows):
    if rows <= 0:
        return []
    
    result = []
    for i in range(1, rows + 1):
        line_chars = []
        if i % 2 == 1:
            for j in range(i):
                line_chars.append(chr(ord('A') + j))
        else:
            for j in range(i - 1, -1, -1):
                line_chars.append(chr(ord('A') + j))
        result.append(''.join(line_chars))
    
    return result

if __name__ == '__main__':
    sample_rows = 5
    pattern = generate_zigzag_triangle(sample_rows)
    for line in pattern:
        print(line)