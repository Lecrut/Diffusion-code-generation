def generate_zigzag_line(width):
    if width <= 0:
        raise ValueError("Width must be greater than 0")

    pattern = []
    for i in range(width):
        if i % 2 == 0:
            line = [' ' * (width - i) + '*' * (2 * i + 1)]
        else:
            line = ['*' * (2 * i + 1) + ' ' * (width - i)]
        pattern.extend(line)

    return '\n'.join(pattern)

if __name__ == '__main__':
    try:
        zigzag_pattern = generate_zigzag_line(5)
        print(zigzag_pattern)
    except ValueError as e:
        print(e)