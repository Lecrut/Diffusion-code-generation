import numpy

def construct_hollow_square_grid(size, outer_value, inner_value):
    grid = numpy.full((size, size), outer_value, dtype=int)
    if size > 2:
        grid[1:-1, 1:-1] = inner_value
    return grid

if __name__ == '__main__':
    size = 5
    outer_val = 1
    inner_val = 0
    result = construct_hollow_square_grid(size, outer_val, inner_val)
    print(result)