def get_diamond_pattern(height: int) -> str:
    rows = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        rows.append(spaces + stars)
    for i in range(height - 1, 0, -1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        rows.append(spaces + stars)
    return '\n'.join(rows)
if __name__ == '__main__':
    half_height = 4
    result = get_diamond_pattern(half_height)
    print(result)