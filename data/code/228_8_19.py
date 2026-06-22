def triangle_pattern():
    n = 5
    for i in range(1, n + 1):
        yield ' '.join(str(j) for j in range(1, i + 1))

if __name__ == '__main__':
    for row in triangle_pattern():
        print(row)