def generate_pattern(rows=10, cols=10):
    pattern = []
    for i in range(rows):
        row = ''.join('*' if (i + j) % 2 == 0 else '.' for j in range(cols))
        pattern.append(row)
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_pattern())