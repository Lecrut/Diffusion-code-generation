def generate_zigzag_line(width):
    pattern = []
    for i in range(width):
        if i % 2 == 0:
            line = [' ' * (width - i - 1) + '*' * (2 * i + 1)]
        else:
            line = ['*' * (2 * i + 1) + ' ' * (width - i - 1)]
        pattern.extend(line)
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_zigzag_line(5))