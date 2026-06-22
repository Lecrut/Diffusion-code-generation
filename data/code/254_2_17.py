def find_min_value(nested_list):
    min_val = float('inf')
    for item in nested_list:
        if isinstance(item, list):
            sub_min = find_min_value(item)
            if sub_min < min_val:
                min_val = sub_min
        elif item < min_val:
            min_val = item
    return min_val

if __name__ == '__main__':
    sample_data = [10, 5, [20, 3], [15, [7]]]
    print(find_min_value(sample_data))