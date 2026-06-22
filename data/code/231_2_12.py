def generate_pattern(rows=10, cols=10):
    pattern = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i + j) % 2 == 0:
                row.append('*')
            else:
                row.append('.')
        pattern.append(''.join(row))
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_pattern())