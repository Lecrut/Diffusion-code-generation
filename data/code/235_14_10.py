def generate_zigzag(width):
    if width < 1:
        raise ValueError("Width must be at least 1")

    pattern = []
    for i in range(width):
        if i % 2 == 0:
            line = [' ' * (width - i - 1) + '*' * (2 * i + 1)]
        else:
            line = ['*' * (2 * i + 1) + ' ' * (width - i - 1)]
        pattern.extend(line)
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_zigzag(5))