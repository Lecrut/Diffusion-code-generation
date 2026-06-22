import numpy

def construct_hollow_square_grid(n):
    if n < 2:
        return numpy.full((n, n), 0, dtype=int)
    grid = numpy.zeros((n, n), dtype=int)
    grid[0, :] = 1
    grid[-1, :] = 1
    grid[:, 0] = 1
    grid[:, -1] = 1
    return grid

if __name__ == '__main__':
    size = 5
    result = construct_hollow_square_grid(size)
    print(result)