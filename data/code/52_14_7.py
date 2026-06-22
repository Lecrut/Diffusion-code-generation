def generate_diamond(size):
    lines = []
    for i in range(1, size + 1):
        lines.append(' ' * (size - i) + '*' * (2 * i - 1))
    for i in range(size - 1, 0, -1):
        lines.append(' ' * (size - i) + '*' * (2 * i - 1))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_diamond(5))