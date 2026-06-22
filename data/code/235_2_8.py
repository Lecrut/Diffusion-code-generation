def generate_diamond_pattern(rows):
    pattern = []
    for i in range(rows):
        spaces = ' ' * (rows - i - 1)
        bars = '|' * (2 * i + 1)
        pattern.append(spaces + bars)
    return pattern

if __name__ == '__main__':
    diamond_rows = 3
    diamond_pattern = generate_diamond_pattern(diamond_rows)
    for line in diamond_pattern:
        print(line)