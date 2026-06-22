def checkerboard(n):
    return [i % 2 ^ (j // n) % 2 for i in range(n * n) for j in range(n)]

if __name__ == '__main__':
    print(checkerboard(8))