def triangle_pattern(n):
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if j % 2 == 0:
                row.append('*')
            else:
                row.append(' ')
        yield ''.join(row)

if __name__ == '__main__':
    for row in triangle_pattern(5):
        print(row)