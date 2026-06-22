def generate_diamond_pattern(half_height):
    pattern = []
    for i in range(1, half_height + 1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        pattern.append(spaces + stars)
    for i in range(half_height - 1, 0, -1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        pattern.append(spaces + stars)
    return pattern
if __name__ == '__main__':
    half_height = 4
    diamond_lines = generate_diamond_pattern(half_height)
    for line in diamond_lines:
        print(line)