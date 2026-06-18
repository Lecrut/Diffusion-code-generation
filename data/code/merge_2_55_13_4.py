import numpy as np
def swap_adjacent(data):
    if isinstance(data, list):
        n = len(data)
        for i in range(n - 1):
            data[i], data[i + 1] = data[i + 1], data[i]
    elif isinstance(data, np.ndarray):
        n = len(data)
        for i in range(n - 1):
            temp = data[i].copy() if hasattr(data[i], 'copy') else data[i]
            data[i] = data[i + 1]
            data[i + 1] = temp
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_array = np.array([1.1, 2.2, 3.3, 4.4])
    swap_adjacent(sample_list)
    print(f"List after swaps: {sample_list}")
    swap_adjacent(sample_array)
    print(f"Numpy array after swaps:\n{sample_array}")