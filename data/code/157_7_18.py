import numpy as np

def find_min_value():
    large_list = [34, 56, 23, 89, 12, 45, 67, 88, 10, 11]
    array = np.array(large_list)
    min_value = np.amin(array)
    return min_value

if __name__ == '__main__':
    print(find_min_value())