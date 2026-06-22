def generate_diamond(height):
    if height <= 0:
        return []
    n = (height + 1) // 2
    upper_rows = [' ' * (n - i) + '*' * (2 * i - 1) for i in range(1, n + 1)]
    lower_rows = [' ' * (i) + '*' * (2 * (n - 1 - i) - 1) for i in range(1, n)]
    lower_rows.reverse()
    return upper_rows + lower_rows

def print_diamond(height):
    rows = generate_diamond(height)
    for row in rows:
        print(row)

if __name__ == '__main__':
    print_diamond(5)
    print_diamond(9)