def generate_star_pyramid(base_width=21):
    rows = (base_width + 1) // 2
    pyramid_lines = []
    for i in range(1, rows + 1):
        stars = '*' * (2 * i - 1)
        padding = ' ' * (rows - i)
        line = padding + stars + padding
        pyramid_lines.append(line)
    return '\n'.join(pyramid_lines)

if __name__ == '__main__':
    result = generate_star_pyramid()
    print(result)