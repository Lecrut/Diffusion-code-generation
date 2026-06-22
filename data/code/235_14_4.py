def generate_zigzag_line(width):
    if width <= 0:
        raise ValueError("Width must be greater than zero")

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
        print(generate_zigzag_line(5))
    except ValueError as e:
        print(e)