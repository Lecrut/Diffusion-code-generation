def triangle_pattern(n):
    for i in range(1, n + 1):
        yield [j for j in range(1, i + 1)]

if __name__ == '__main__':
    for row in triangle_pattern(5):
        print(' '.join(map(str, row)))