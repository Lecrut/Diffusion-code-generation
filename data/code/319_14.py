import numpy as np
if __name__ == '__main__':
    rows = 5
    cols = 10
    min_val = 1
    max_val = 100
    grid = np.random.randint(min_val, max_val + 1, size=(rows, cols))
    print(grid)