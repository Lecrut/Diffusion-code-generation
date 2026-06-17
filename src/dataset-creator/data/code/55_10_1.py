def swap_adjacent(data: list | tuple, index: int = None) -> list:
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    n = len(data)
    if n == 0:
        return []
    result_list = list(data)
    if n < 2 and index is None:
        return result_list
    if index is not None:
        if not (0 <= index < n - 1):
            raise IndexError("Index out of range for adjacent swap.")
        temp = result_list[index]
        result_list[index] = result_list[index + 1]
        result_list[index + 1] = temp
    else:
        raise ValueError("An index must be provided to specify which pair to swap.")
    return result_list
if __name__ == '__main__':
    sample_data = [4, 2, 9, 7, 5]
    swapped_result = swap_adjacent(sample_data, index=1)
    print(swapped_result)