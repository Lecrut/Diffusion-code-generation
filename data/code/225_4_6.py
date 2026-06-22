def find_min_max(nested_list):
    min_val = float('inf')
    max_val = float('-inf')
    for item in nested_list:
        if isinstance(item, list):
            sub_min, sub_max = find_min_max(item)
            min_val = min(min_val, sub_min)
            max_val = max(max_val, sub_max)
        else:
            min_val = min(min_val, item)
            max_val = max(max_val, item)
    return min_val, max_val

if __name__ == '__main__':
    sample_list = [3, [1, 2], [5, [4, 6]], 7]
    print(find_min_max(sample_list))