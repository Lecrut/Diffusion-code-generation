import collections
def swap_adjacent_values(data):
    if isinstance(data, set):
        data_list = sorted(list(data))
    elif not hasattr(data, '__getitem__'):
        raise TypeError("Input must be iterable or convertible to sequence.")
    else:
        data_list = list(data)
    for i in range(0, len(data_list), 2):
        if i + 1 < len(data_list):
            data_list[i], data_list[i + 1] = data_list[i + 1], data_list[i]
    return data_list
if __name__ == '__main__':
    sample_set = {5, 3, 8, 2}
    result = swap_adjacent_values(sample_set)
    print(result)