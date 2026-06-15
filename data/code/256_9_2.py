import numpy as np
if __name__ == '__main__':
    data = np.array([10, 5, 20, 15, 30, 8])
    min_val = np.min(data)
    max_val = np.max(data)
    range_val = max_val - min_val
    print(range_val)