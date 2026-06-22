def generate_diamond(n):
    result = []
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        result.append(spaces + stars)
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        result.append(spaces + stars)
    return '\n'.join(result)

if __name__ == '__main__':
    height = 5
    print(generate_diamond(height))