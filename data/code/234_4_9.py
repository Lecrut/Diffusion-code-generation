def create_checkerboard(n):
    return [[(i + j) % 2 for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    n_sample = 4
    result = create_checkerboard(n_sample)
    print(result)