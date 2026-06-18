def swap_adjacent(data: list | tuple, index: int = None) -> any:
    if not data:
        return data
    n = len(data)
    if n == 1:
        return data
    if index is None or not isinstance(index, int):
        target_index = max(0, min(n - 2, len(data)))
    else:
        target_index = max(0, min(len(data) - 1, index))
    if target_index + 1 >= n:
        return data
    is_tuple = isinstance(data, tuple)
    if is_tuple:
        new_data = list(data)
        new_data[target_index], new_data[target_index + 1] = new_data[target_index + 1], new_data[target_index]
        return tuple(new_data)
    else:
        new_data = list(data)
        new_data[target_index], new_data[target_index + 1] = new_data[target_index + 1], new_data[target_index]
        return new_data
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (5, 6, 7)
    result_list = swap_adjacent(sample_list)
    result_tuple = swap_adjacent(sample_tuple, index=0)
    print(f"Original List: {sample_list}")
    print(f"Swapped List:   {result_list}")
    print(f"Original Tuple: {sample_tuple}")
    print(f"Swapped Tuple:  {result_tuple}")
    empty_result = swap_adjacent([])
    single_result = swap_adjacent([42])
    print(f"\nEmpty List Result:   {empty_result}")
    print(f"Single Element Result: {single_result}")