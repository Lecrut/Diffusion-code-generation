def find_extremes(nested_list):
    min_val = float('inf')
    max_val = float('-inf')
    for sublist in nested_list:
        if isinstance(sublist, list):
            sub_min, sub_max = find_extremes(sublist)
            min_val = min(min_val, sub_min)
            max_val = max(max_val, sub_max)
        else:
            min_val = min(min_val, sublist)
            max_val = max(max_val, sublist)
    return min_val, max_val

if __name__ == '__main__':
    sample_list = [[3, 5], [1, 2, [4, 6]], 7, [8, 9]]
    print(find_extremes(sample_list))