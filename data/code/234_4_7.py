N_ROWS = 4
N_COLS = 4

def create_checkerboard(n):
    return [i % 2 ^ j % 2 for i in range(n * n)]

if __name__ == '__main__':
    sample_n = N_ROWS * N_COLS
    result = create_checkerboard(sample_n)
    print(result)