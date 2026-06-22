def find_min_value(nested_list):
    min_val = float('inf')
    for item in nested_list:
        if isinstance(item, list):
            min_val = min(find_min_value(item), min_val)
        else:
            min_val = min(item, min_val)
    return min_val

if __name__ == '__main__':
    sample_data = [3, 5, [1, 2], [4, [0, -1]]]
    print(find_min_value(sample_data))