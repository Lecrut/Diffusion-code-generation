def find_max_in_nested_list(nested_list):
    max_value = float('-inf')
    for item in nested_list:
        if isinstance(item, list):
            current_max = find_max_in_nested_list(item)
            if current_max > max_value:
                max_value = current_max
        else:
            if item > max_value:
                max_value = item
    return max_value

if __name__ == '__main__':
    sample_data = [1, [2, 3, [4, 5]], 6, [7, [8, [9, 10]]], 11]
    result = find_max_in_nested_list(sample_data)
    print(result)