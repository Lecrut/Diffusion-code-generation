def find_min_in_nested_list(nested_list):
    min_val = float('inf')
    for item in nested_list:
        if isinstance(item, list):
            min_item = find_min_in_nested_list(item)
        else:
            min_item = item
        if min_item < min_val:
            min_val = min_item
    return min_val

if __name__ == '__main__':
    sample_data = [[3, 5], [1, 2], [4]]
    print(find_min_in_nested_list(sample_data))