def generate_pyramid_pattern(rows):
    if not isinstance(rows, int) or rows <= 0:
        return []
    
    result = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        letters = ''.join(chr(64 + j) for j in range(1, i + 1))
        row_str = spaces + letters
        result.append(row_str)
    return result

if __name__ == '__main__':
    pattern = generate_pyramid_pattern(5)
    for line in pattern:
        print(line)