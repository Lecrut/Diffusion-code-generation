def print_pyramid(base_width=21):
    lines = []
    for i in range(1, base_width + 1, 2):
        stars = '*' * i
        spaces = ' ' * ((base_width - i) // 2)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_pyramid())