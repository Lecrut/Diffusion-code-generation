def generate_diamond_pattern(half_height):
    diamond_lines = []
    for i in range(1, half_height + 1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        diamond_lines.append(spaces + stars)
    for i in range(half_height - 1, 0, -1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        diamond_lines.append(spaces + stars)
    return '\n'.join(diamond_lines)

if __name__ == '__main__':
    half_height = 4
    print(generate_diamond_pattern(half_height))