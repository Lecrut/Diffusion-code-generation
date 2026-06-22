import numpy as np

def construct_hollow_square(n, fill_char='*', empty_char=' '):
    if n <= 0:
        return np.array([])
    grid = np.full((n, n), empty_char, dtype=object)
    if n >= 1:
        grid[0, :] = fill_char
        grid[-1, :] = fill_char
        grid[:, 0] = fill_char
        grid[:, -1] = fill_char
    return grid

if __name__ == '__main__':
    sample_n = 5
    result = construct_hollow_square(sample_n, '*', ' ')
    print(result.tolist())