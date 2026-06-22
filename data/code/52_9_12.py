def generate_diamond_pattern(half_height: int) -> str:
    lines = []
    for i in range(1, half_height + 1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(half_height - 1, 0, -1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)
if __name__ == '__main__':
    pattern = generate_diamond_pattern(4)
    print(pattern)