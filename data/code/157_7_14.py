import numpy as np

def find_smallest_value():
    data = [34, 56, 23, 89, 12, 45, 67, 88, 90, 11]
    return np.amin(data)

if __name__ == '__main__':
    print(find_smallest_value())