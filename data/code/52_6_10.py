def generate_diamond(size):
    lines = []
    half = size // 2
    for i in range(size):
        if i <= half:
            spaces = half - i
            stars = 2 * i + 1
        else:
            spaces = i - half
            stars = 2 * (size - 1 - i) + 1
        line = ' ' * spaces + '*' * stars + ' ' * spaces
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    size = 8
    print(generate_diamond(size))