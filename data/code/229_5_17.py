import numpy as np

def create_sequential_grid(side_length):
    if not isinstance(side_length, int) or side_length < 1:
        raise ValueError("Side length must be a positive integer")
    
    sequential_values = np.arange(side_length * side_length)
    grid = sequential_values.reshape((side_length, side_length))
    return grid

if __name__ == '__main__':
    sample_side_length = 4
    try:
        grid = create_sequential_grid(sample_side_length)
        print(grid)
    except ValueError as e:
        print(e)