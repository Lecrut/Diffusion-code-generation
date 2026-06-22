def generate_zigzag_triangle(rows):
    if rows <= 0:
        return ""
    
    lines = []
    current_char = ord('A')
    
    for i in range(1, rows + 1):
        line_chars = []
        for j in range(i):
            line_chars.append(chr(current_char))
            current_char += 1
            if current_char > ord('Z'):
                current_char = ord('A')
        lines.append(''.join(line_chars))
    
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_zigzag_triangle(5)
    print(result)