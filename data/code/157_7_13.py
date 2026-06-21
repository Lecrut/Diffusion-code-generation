import numpy as np

def find_min_value():
    large_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    array = np.array(large_list)
    min_value = np.amin(array)
    return min_value

if __name__ == '__main__':
    print(find_min_value())