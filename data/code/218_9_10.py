import numpy as np

def find_min_value():
    data = np.array([34, 23, 56, 12, 89, 45])
    return np.min(data)

if __name__ == '__main__':
    print(find_min_value())