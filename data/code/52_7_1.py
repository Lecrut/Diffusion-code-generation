def create_diamond_pattern(n):
    pattern = []
    for i in range(n):
        pattern.append(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        pattern.append(' ' * (n - i - 1) + '*' * (2 * i + 1))
    return '\n'.join(pattern)

if __name__ == '__main__':
    sample_value = 5
    result = create_diamond_pattern(sample_value)
    print(result)