def generate_diamond(n):
    result = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        result.append(spaces + stars)
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        result.append(spaces + stars)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_diamond(8))