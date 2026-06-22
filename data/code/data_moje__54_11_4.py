import numpy as np

def create_hollow_square_grid(size: int, hollow_char: int = 0, fill_char: int = 1) -> np.ndarray:
    if size < 1:
        raise ValueError("Size must be at least 1")
    grid = np.full((size, size), fill_char, dtype=int)
    if size > 2:
        grid[1:-1, 1:-1] = hollow_char
    return grid

if __name__ == '__main__':
    sample_size = 6
    result_grid = create_hollow_square_grid(sample_size, hollow_char=0, fill_char=1)
    print(result_grid)