def generate_pattern(rows, cols):
    if rows <= 0 or cols <= 0:
        return []

    pattern = []
    for i in range(rows):
        row = ['*'] * i + ['.'] * (cols - i)
        pattern.append(row)

    return pattern

if __name__ == '__main__':
    rows_val = 10
    cols_val = 10
    pattern = generate_pattern(rows_val, cols_val)
    for row in pattern:
        print(' '.join(row))