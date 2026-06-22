import numpy as np

def find_min_value():
    data = np.array([34, 23, 56, 12, 89, 0, -1])
    return np.min(data)

if __name__ == '__main__':
    min_value = find_min_value()
    print(min_value)