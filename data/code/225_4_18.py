def find_min_max(nested_list):
    min_val = float('inf')
    max_val = float('-inf')
    for item in nested_list:
        if isinstance(item, list):
            sub_min, sub_max = find_min_max(item)
            if sub_min < min_val:
                min_val = sub_min
            if sub_max > max_val:
                max_val = sub_max
        elif item < min_val:
            min_val = item
        elif item > max_val:
            max_val = item
    return (min_val, max_val)
if __name__ == '__main__':
    sample_data = [10, 5, [20, 3], 15, [25, [30, 4]]]
    print(find_min_max(sample_data))