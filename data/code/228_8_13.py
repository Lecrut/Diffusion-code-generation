def triangle_pattern(n):
    MAX_WIDTH = 2 * n - 1
    for i in range(1, n + 1):
        row = [' ' * ((MAX_WIDTH - (2 * i - 1)) // 2)]
        for j in range(i):
            row.append('*')
        yield ''.join(row)

if __name__ == '__main__':
    for row in triangle_pattern(5):
        print(row)