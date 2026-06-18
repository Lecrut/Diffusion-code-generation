def swap_adjacent(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    n = len(values)
    try:
        index_a = int(input(f"Enter first zero-based index ({n - 1}): "))
        index_b = int(input(f"Enter second adjacent zero-based index (must differ by 1): "))
        if not isinstance(index_a, int) or not isinstance(index_b, int):
            raise ValueError("Indices must be integers.")
        if abs(index_a - index_b) != 1:
            raise IndexError("Selected indices are not adjacent.")
        min_idx = min(index_a, index_b)
        if min_idx < 0 or max(min_idx + (index_a > index_b), index_b) >= n:
            raise IndexError(f"Indices out of range for list of length {n}.")
    except ValueError as ve:
        print(f"Invalid input type: {ve}")
        return values
    if isinstance(values, tuple):
        data = list(values)
    a, b = index_a, index_b
    if a > 0 and b == a - 1 or a < n - 1 and b == a + 1:
        temp = data[a]
        data[a] = data[b]
        data[b] = temp
        return tuple(data) if isinstance(values, tuple) else data
if __name__ == '__main__':
    sample_list = [40, 35, 28, 19, 76]
def swap_adjacent_hardcoded(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    n = len(values)
    idx_a, idx_b = 1, 2
    if abs(idx_a - idx_b) != 1:
        raise IndexError("Selected hardcoded indices are not adjacent.")
    min_idx = min(idx_a, idx_b)
    if min_idx < 0 or max(min_idx + (idx_a > idx_b), idx_b) >= n:
        raise IndexError(f"Hardcoded indices out of range for list of length {n}.")
    data = values[:]                                                                               
    if isinstance(values, tuple):
        temp = data[idx_a]
        data[idx_a] = data[idx_b]
        data[idx_b] = temp
        return tuple(data)
    else:
        temp = data[idx_a]
        data[idx_a] = data[idx_b]
        data[idx_b] = temp
if __name__ == '__main__':
    sample_values = [40, 35, 28, 19, 76]
    try:
        result = swap_adjacent_hardcoded(sample_values)
        print(f"Original List: {sample_values}")
        print(f"Swapped Result (indices 1 and 2): {result}")
        sample_tuple = ("apple", "banana", "cherry")
        result_tup = swap_adjacent_hardcoded(sample_tuple)
        print(f"Original Tuple: {sample_tuple}")
        print(f"Swapped Result (indices 0 and 1): {result_tup}")
    except Exception as e:
        print(f"Error occurred during execution: {e}")