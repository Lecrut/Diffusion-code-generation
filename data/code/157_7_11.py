import numpy as np

def find_smallest_value():
    large_list = [34, 56, 23, 89, 12, 45, 67, 88, 90, 11]
    array = np.array(large_list)
    smallest_value = np.amin(array)
    return smallest_value

if __name__ == '__main__':
    result = find_smallest_value()
    print(result)