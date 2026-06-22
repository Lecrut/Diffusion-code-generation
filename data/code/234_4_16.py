checkerboard_pattern = {0: 1, 1: 0}

def create_checkerboard(n):
    return [checkerboard_pattern[(i + j) % 2] for i in range(n) for j in range(n)]

if __name__ == '__main__':
    n_sample = 4
    result = create_checkerboard(n_sample)
    print(result)