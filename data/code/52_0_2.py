def generate_diamond_pattern(size):
    pattern = []
    for i in range(1, size + 1, 2):
        spaces = (size - i) // 2
        stars = '*' * i
        line = ' ' * spaces + stars
        pattern.append(line)
    for i in range(size - 2, 0, -2):
        spaces = (size - i) // 2
        stars = '*' * i
        line = ' ' * spaces + stars
        pattern.append(line)
    return pattern
if __name__ == '__main__':
    size = 5
    diamond_lines = generate_diamond_pattern(size)
    for line in diamond_lines:
        print(line)