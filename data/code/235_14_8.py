def generate_zigzag(width):
    if width <= 0:
        raise ValueError("Width must be greater than zero")

    pattern = []
    for i in range(width):
        if i % 2 == 0:
            line = '*' * (i + 1)
        else:
            line = ' ' * (width - i - 1) + '*' * (i + 1)
        pattern.append(line)

    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_zigzag(5))