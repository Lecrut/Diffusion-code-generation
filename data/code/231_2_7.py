def generate_pattern(rows=10, cols=10):
    pattern = []
    for i in range(rows):
        row = ''
        for j in range(cols):
            if (i + j) % 2 == 0:
                row += '*'
            else:
                row += '.'
        pattern.append(row)
    return pattern

if __name__ == '__main__':
    pattern = generate_pattern()
    for row in pattern:
        print(row)