import collections
def swap_adjacent_values(data_structure):
    if isinstance(data_structure, set):
        data_list = sorted(list(data_structure))
    elif hasattr(data_structure, '__iter__') and not isinstance(data_structure, str) and type(data_structure).__name__ in ['list', 'tuple']:
        if type(data_structure).__name__ == 'tuple':
            data_list = list(data_structure)
        else:
            data_list = data_structure.copy()
    elif hasattr(data_structure, '__iter__'):
        raise TypeError("Unsupported input type. Expected list, set, tuple or similar sequence.")
    else:
        raise TypeError(f"Input must be an iterable (list/set/tuple), got {type(data_structure).__name__}")
    n = len(data_list)
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            temp = data_list[i]
            data_list[i] = data_list[i + 1]
            data_list[i + 1] = temp
    return data_list
if __name__ == '__main__':
    set_input = {3, 5, 2, 8}
    list_input = [40, 60, 70, 90]
    result_set_swap = swap_adjacent_values(set_input)
    result_list_swap = swap_adjacent_values(list_input)
    print("Swapped Set (converted to sorted list):", result_set_swap)
    print("Swapped List:", result_list_swap)