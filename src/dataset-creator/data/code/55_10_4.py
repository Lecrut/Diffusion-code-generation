def swap_adjacent(data: list | tuple, index: int = None) -> list | tuple:
    if not data:
        return [] if isinstance(data, list) else ()
    length = len(data)
    if length < 2:
        return data
    target_index = index if index is not None else 0
    try:
        if isinstance(data, list):
            original_list = data[:]
            swapped_data = [data[i] for i in range(length)]
            temp = swapped_data[target_index]
            swapped_data[target_index], swapped_data[target_index + 1] = swapped_data[target_index + 1], temp
            return swapped_data
        else:
            original_tuple = tuple(data)
            converted_list = list(original_tuple)
            if target_index < length - 1:
                temp = converted_list[target_index]
                converted_list[target_index], converted_list[target_index + 1] = converted_list[target_index + 1], temp
            return converted_list
    except IndexError:
        return data
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c')
    result_list = swap_adjacent(sample_list)
    print(f"Swapped List: {result_list}")
    swapped_specific_list = swap_adjacent(result_list, index=1)
    print(f"Specifically Swapped List: {swapped_specific_list}")
    result_tuple = swap_adjacent(sample_tuple)
    print(f"Swapped Tuple: {result_tuple}")