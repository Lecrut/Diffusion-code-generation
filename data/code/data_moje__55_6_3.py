def hollow_alphabet_triangle(base_width):
    if base_width < 1:
        return []
    
    lines = []
    for i in range(1, base_width + 1):
        row = []
        for j in range(1, i + 1):
            if i == 1 or i == base_width or j == 1 or j == i:
                char = chr(64 + j)
                row.append(char)
            else:
                row.append(' ')
        lines.append(''.join(row))
    return lines

if __name__ == '__main__':
    base = 5
    result = hollow_alphabet_triangle(base)
    for line in result:
        print(line)