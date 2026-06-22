def generate_pyramid(base_width=21):
    if base_width % 2 == 0:
        base_width -= 1
    lines = []
    for i in range(1, base_width + 1, 2):
        stars = '*' * i
        spaces = ' ' * ((base_width - i) // 2)
        lines.append(spaces + stars + spaces)
    return '\n'.join(lines)
if __name__ == '__main__':
    pyramid = generate_pyramid(21)
    print(pyramid)