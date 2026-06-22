def build_pyramid(base_width=21):
    lines = []
    for i in range(1, base_width + 1, 2):
        spaces = ' ' * ((base_width - i) // 2)
        stars = '*' * i
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(build_pyramid())