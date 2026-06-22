def generate_diamond(n):
    if n <= 0:
        return []
    rows = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        rows.append(spaces + stars.rstrip())
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        rows.append(spaces + stars.rstrip())
    return rows

if __name__ == '__main__':
    n = 5
    result = generate_diamond(n)
    for line in result:
        print(line)