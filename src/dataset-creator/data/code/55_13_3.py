import numpy as np
def swap_adjacent(data):
    if isinstance(data, list):
        for i in range(len(data) - 1):
            data[i], data[i + 1] = data[i + 1], data[i]
    elif isinstance(data, np.ndarray):
        for i in range(len(data) - 1):
            temp = data[i].copy() if hasattr(data[i], 'copy') else data[i]
            data[i] = data[i + 1]
            data[i + 1] = temp
if __name__ == '__main__':
    sample_list = [5, 2, 8, 3, 9]
    sample_array = np.array([7.0, 4.0, 6.0])
    swap_adjacent(sample_list)
    swap_adjacent(sample_array)