import numpy as np
if __name__ == '__main__':
    data = np.array([10, 5, 20, 15, 30, 8, 25])
    min_val = np.min(data)
    max_val = np.max(data)
    data_range = max_val - min_val
    print(data_range)