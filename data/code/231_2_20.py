def generate_pattern(rows, cols):
    pattern = []
    for i in range(rows * cols):
        row = (i // cols) % 2 == 0
        col = i % cols
        if col % 2 == 0:
            pattern.append('*' if row else '.')
        else:
            pattern.append('.' if row else '*')
    return [pattern[i:i + cols] for i in range(0, len(pattern), cols)]

if __name__ == '__main__':
    rows = 10
    cols = 10
    pattern = generate_pattern(rows, cols)
    for row in pattern:
        print(' '.join(row))