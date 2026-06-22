def generate_zigzag(width):
    zigzag = []
    for i in range(width):
        if i % 2 == 0:
            line = '*' * (i + 1)
        else:
            line = ' ' * (width - i - 1) + '*' * (i + 1)
        zigzag.append(line)
    return '\n'.join(zigzag)

if __name__ == '__main__':
    print(generate_zigzag(5))