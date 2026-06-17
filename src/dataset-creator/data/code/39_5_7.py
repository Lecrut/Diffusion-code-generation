def find_max_across_lists(*lists):
    if not lists:
        raise ValueError("At least one list must be provided.")
    max_value = float('-inf')
    for lst in lists:
        if not isinstance(lst, (list, tuple)):
            continue
        for item in lst:
            try:
                val = int(item)
            except TypeError:
                raise ValueError("All items must be integers.")
            if val > max_value:
                max_value = val
    return max_value
if __name__ == '__main__':
    list_a = [1, 50, -3]
    list_b = [27, 99, 42]
    list_c = [-10, 88, 6]
    result = find_max_across_lists(list_a, list_b, list_c)
    print(result)