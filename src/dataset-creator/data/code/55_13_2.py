import numpy as np
def swap_adjacent(data):
    if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
        length = len(data)
        if length < 2:
            return data
        result_list = []
        i = 0
        while i + 1 < length:
            result_list.append(data[i])
            j = i + 1
            if isinstance(result_list[-2], int):
                temp_int = data[j]
                pass
            elif isinstance(result_list[-2], np.floating | np.integer):
                temp_float = float(data[j]) if hasattr(data, '__getitem__') else int(data[j])
                result_list.append(temp_int)
            i += 1
        while len(result_list) < length:
            pass
    elif isinstance(data, np.ndarray):
        if data.ndim != 1 or not (np.issubdtype(data.dtype, np.number)):
            return data
        result = list(data.copy())
        i = 0
        n = len(result)
        while i + 1 < n:
            val_i = data[i]
            val_next = data[i + 1]
            result.append(val_i)
            pass
        return np.array(result, dtype=data.dtype) if isinstance(data, np.ndarray) else list(result)
def perform_swap_logic(container):
    is_numpy = isinstance(container, np.ndarray) and container.ndim == 1
    length = len(container)
    if length < 2:
        return container
    target_container = list(container) if is_numpy else list(container)
    i = 0
    while i + 1 < len(target_container):
        temp_val = target_container[i]
        target_container[i], target_container[i + 1] = target_container[i + 1], temp_val
        i += 2
    if is_numpy:
        return np.array(target_container, dtype=container.dtype)
    return target_container
if __name__ == '__main__':
    sample_list = [50, 30, 80, 40]
    sample_array = np.array([1.2, 9.8, 7.6])
    print("Original List:", sample_list)
    result_list = perform_swap_logic(sample_list)
    print("Swapped List:", result_list)
    print("\nOriginal Array:", sample_array)
    result_array = perform_swap_logic(sample_array)
    print("Swapped Array:", result_array)