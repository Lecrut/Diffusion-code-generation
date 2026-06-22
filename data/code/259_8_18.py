def find_extremes(nested_list):
    if not nested_list:
        return (None, None)
    min_val = float('inf')
    max_val = float('-inf')
    for sublist in nested_list:
        if isinstance(sublist, list):
            sub_min, sub_max = find_extremes(sublist)
            if sub_min is not None and sub_min < min_val:
                min_val = sub_min
            if sub_max is not None and sub_max > max_val:
                max_val = sub_max
        else:
            if sublist < min_val:
                min_val = sublist
            if sublist > max_val:
                max_val = sublist
    return (min_val, max_val)
if __name__ == '__main__':
    sample_list = [[3, 5], [1, 2], [4, 6], [7]]
    print(find_extremes(sample_list))