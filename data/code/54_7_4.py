def generate_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    top_bottom = '*' * n
    middle = '*' + ' ' * (n - 2) + '*'
    rows = [top_bottom]
    for _ in range(n - 2):
        rows.append(middle)
    rows.append(top_bottom)
    return rows

if __name__ == '__main__':
    result = generate_hollow_square(5)
    for row in result:
        print(row)