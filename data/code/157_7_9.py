import numpy as np

def find_smallest_value():
    data = [34, 56, 23, 89, 12, 45, 67, 88, 10, 11]
    return np.amin(data)

if __name__ == '__main__':
    smallest_value = find_smallest_value()
    print(smallest_value)