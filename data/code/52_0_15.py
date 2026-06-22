def generate_diamond_pattern(size):
    pattern = []
    for i in range(1, size + 1):
        line = ' ' * (size - i) + '*' * (2 * i - 1)
        pattern.append(line)
    for i in range(size - 1, 0, -1):
        line = ' ' * (size - i) + '*' * (2 * i - 1)
        pattern.append(line)
    return pattern
if __name__ == '__main__':
    result = generate_diamond_pattern(5)
    for line in result:
        print(line)