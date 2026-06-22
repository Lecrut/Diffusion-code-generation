def triangle_pattern(n):
    for i in range(1, n + 1):
        yield [1] * i

if __name__ == '__main__':
    for row in triangle_pattern(5):
        print(row)