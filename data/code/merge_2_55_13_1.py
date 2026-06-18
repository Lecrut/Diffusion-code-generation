import numpy as np
def swap_adjacent(data):
    if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
        length = len(data)
        if length < 2:
            return data
        i = 0
        while i + 1 < length:
            temp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = temp
            i += 2
    elif isinstance(data, np.ndarray):
        if len(data) == 0 or (len(data.shape) > 1 and not all(len(s) < 2 for s in data.shape)):
            return data.copy()
        flat_data = data.flatten().tolist()
        length = len(flat_data)
        i = 0
        while i + 1 < length:
            temp = flat_data[i]
            flat_data[i] = flat_data[i + 1]
            flat_data[i + 1] = temp
            i += 2
    return data
if __name__ == '__main__':
    sample_list = [5, 3, 8, 4, 9, 7]
    sample_array = np.array([60.5, 20.1, 90.3])
    print("Original List:", sample_list)
    result_list = swap_adjacent(sample_list.copy())
    print("Swapped List:", result_list)
    print("\nOriginal Array:", sample_array)
    result_array = swap_adjacent(sample_array.copy())
    print("Swapped Array:", result_array)