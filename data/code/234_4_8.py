def create_checkerboard(n):
    return [[1 if (i + j) % 2 == 0 else 0 for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    n_sample = 6
    result = create_checkerboard(n_sample)
    print(result)