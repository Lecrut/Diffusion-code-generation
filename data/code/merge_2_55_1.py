def swap_adjacent(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    result = []
    for i in range(0, len(iterable), 2):
        if i + 1 < len(iterable):
            result.append((iterable[i], iterable[i+1]))
        else:
            result.append(iterable[i])
    return tuple(result)
def swap_adjacent_list(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            data[i], data[i+1] = data[i+1], data[i]
    return data
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (6, 7, 8)
    swapped_list_result = swap_adjacent(sample_list.copy())
    print(f"List after swap: {swapped_list_result}")
    swapped_tuple_result = swap_adjacent(tuple([9, 10]))
    print(f"Tuple result: {swapped_tuple_result}")