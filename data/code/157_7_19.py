import numpy as np

def find_smallest_value():
    large_list = [34, 56, 23, 89, 12, 45, 67, 90, 11, 22]
    array = np.array(large_list)
    smallest_value = np.amin(array)
    return smallest_value

if __name__ == '__main__':
    print(find_smallest_value())