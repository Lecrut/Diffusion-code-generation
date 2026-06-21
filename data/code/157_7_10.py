import numpy as np

def find_smallest_value():
    data = [34, 56, 23, 89, 12, 45, 67, 88, 90, 11]
    arr = np.array(data)
    smallest_value = np.amin(arr)
    return smallest_value

if __name__ == '__main__':
    result = find_smallest_value()
    print(result)