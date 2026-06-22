import numpy as np

def find_min_value():
    data = np.array([3, 5, 1, 2, 4])
    return np.min(data)

if __name__ == '__main__':
    print(find_min_value())