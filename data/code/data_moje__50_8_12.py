def print_star_pyramid(base_width):
    if base_width % 2 == 0:
        base_width -= 1
    lines = []
    for i in range(1, base_width + 1, 2):
        spaces = ' ' * ((base_width - i) // 2)
        stars = '*' * i
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = print_star_pyramid(21)
    print(result)