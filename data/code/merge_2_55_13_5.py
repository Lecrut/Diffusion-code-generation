import numpy as np
def swap_adjacent(data):
    if isinstance(data, list) and len(data) > 1:
        for i in range(len(data) - 2, 0, -2):
            data[i], data[i + 1] = data[i + 1], data[i]
    elif isinstance(data, np.ndarray):
        if data.ndim == 1 and len(data) > 1:
            for i in range(len(data) - 2, 0, -2):
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
if __name__ == '__main__':
    sample_list = [5, 4, 3, 2, 1]
    sample_array = np.array([90, 80, 70, 60, 50])
    swap_adjacent(sample_list)
    print(f"List after swap: {sample_list}")
    swap_adjacent(sample_array)
    print(f"Numpy array after swap:\n{sample_array}")