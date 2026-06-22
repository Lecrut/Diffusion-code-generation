def find_max_in_nested_list(nested_list):
    max_value = float('-inf')
    for item in nested_list:
        if isinstance(item, list):
            max_value = max(max_value, find_max_in_nested_list(item))
        else:
            max_value = max(max_value, item)
    return max_value

if __name__ == '__main__':
    sample_data = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10, 11]]]
    print(find_max_in_nested_list(sample_data))