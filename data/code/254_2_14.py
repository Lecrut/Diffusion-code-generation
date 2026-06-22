def find_min_in_nested_list(nested_list):
    min_val = float('inf')
    for item in nested_list:
        if isinstance(item, list):
            item_min = find_min_in_nested_list(item)
        else:
            item_min = item
        if item_min < min_val:
            min_val = item_min
    return min_val

if __name__ == '__main__':
    sample_data = [[3, 5, [1, 2]], 4, [6, [7, 8], 9]]
    print(find_min_in_nested_list(sample_data))