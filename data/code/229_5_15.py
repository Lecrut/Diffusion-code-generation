import numpy as np

def create_sequential_grid(size):
    if size <= 0:
        raise ValueError("Size must be greater than zero")
    
    total_elements = size ** 2
    sequential_values = np.arange(total_elements)
    grid = sequential_values.reshape((size, size))
    return grid

if __name__ == '__main__':
    sample_grid = create_sequential_grid(4)
    print(sample_grid)