def checkerboard(n):
    return [i % 2 for i in range(n * n)]

if __name__ == '__main__':
    print(checkerboard(4))