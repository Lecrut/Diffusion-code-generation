def triangle_pattern(n):
    for i in range(1, n + 1):
        row = [str(j) for j in range(1, i + 1)]
        yield ' '.join(row)

if __name__ == '__main__':
    pattern = triangle_pattern(7)
    for _ in range(5):
        print(next(pattern))