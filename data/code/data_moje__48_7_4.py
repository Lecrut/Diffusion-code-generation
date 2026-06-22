def find_largest(nested_list):
    max_value = None
    for item in nested_list:
        if isinstance(item, list):
            current_max = find_largest(item)
        else:
            current_max = item
        if max_value is None or current_max > max_value:
            max_value = current_max
    return max_value

if __name__ == '__main__':
    sample_data = [1, [2, 3, [4, 5]], 6, [7, [8, 9, [10, 11]]]]
    result = find_largest(sample_data)
    print(result)