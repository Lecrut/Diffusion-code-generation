import numpy as np

def construct_hollow_square_grid(n, border_char='*', interior_char=' '):
    if n <= 0:
        return np.array([])
    grid = np.full((n, n), interior_char, dtype='<U1')
    if n > 0:
        grid[0, :] = border_char
        grid[-1, :] = border_char
        grid[:, 0] = border_char
        grid[:, -1] = border_char
    return grid

if __name__ == '__main__':
    result = construct_hollow_square_grid(5)
    print(result)