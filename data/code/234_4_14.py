def checkerboard(n):
    return [i % 2 == j % 2 for i in range(n) for j in range(n)]

if __name__ == '__main__':
    print(checkerboard(4))