def triangle_pattern(n):
    for i in range(1, n + 1):
        yield ' '.join(str(j) for j in range(1, i + 1))

if __name__ == '__main__':
    pattern = triangle_pattern(7)
    for row in pattern:
        print(row)