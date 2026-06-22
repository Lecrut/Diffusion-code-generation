def generate_diamond_pattern(half_height):
    lines = []
    for i in range(1, half_height + 1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(half_height - 1, 0, -1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return lines

def print_diamond_pattern(half_height):
    pattern = generate_diamond_pattern(half_height)
    for line in pattern:
        print(line)
if __name__ == '__main__':
    half_height = 4
    print_diamond_pattern(half_height)