import collections
def swap_adjacent(data):
    if isinstance(data, set):
        data_list = sorted(list(data))
    elif hasattr(data, '__iter__') and not isinstance(data, str):
        data_list = list(data)
    else:
        raise TypeError("Input must be iterable or convertible to list.")
    for i in range(0, len(data_list), 2):
        if i + 1 < len(data_list):
            data_list[i], data_list[i + 1] = data_list[i + 1], data_list[i]
    return data_list
if __name__ == '__main__':
    sample_set = {5, 3, 8, 2}
    result = swap_adjacent(sample_set)
    print(result)