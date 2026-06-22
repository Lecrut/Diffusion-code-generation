def generate_diamond(rows):
    result = []
    n = rows // 2
    for i in range(-n, n + 1):
        abs_i = abs(i)
        spaces = ' ' * (n - abs_i)
        stars = '*' * (2 * abs_i + 1)
        result.append(spaces + stars + spaces)
    return result

if __name__ == '__main__':
    rows = 5
    lines = generate_diamond(rows)
    for line in lines:
        print(line)