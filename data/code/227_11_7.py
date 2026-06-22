def generate_star_pattern(n):
    pattern = []
    for i in range(1, n + 1):
        row = '*' * (2 * i - 1)
        padding = ' ' * (n - i)
        pattern.append(padding + row + padding)
    return pattern

if __name__ == '__main__':
    result = generate_star_pattern(4)
    for line in result:
        print(line)