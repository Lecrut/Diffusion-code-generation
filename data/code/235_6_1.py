def triangle_generator(n):
    for i in range(1, n + 1):
        yield "*" * i
if __name__ == '__main__':
    N = 5
    for line in triangle_generator(N):
        print(line)