def generate_diamond(n):
    result = []
    for i in range(n):
        spaces = ' ' * (n - 1 - i)
        stars = '*' * (2 * i + 1)
        result.append(spaces + stars)
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - 1 - i)
        stars = '*' * (2 * i + 1)
        result.append(spaces + stars)
    return result

if __name__ == '__main__':
    dimension = 6
    lines = generate_diamond(dimension)
    for line in lines:
        print(line)