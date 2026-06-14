def triangle_generator(n):
    for i in range(1, n + 1):
        line = "*" * i
        yield line
if __name__ == '__main__':
    N = 5
    triangle = triangle_generator(N)
    for line in triangle:
        print(line)