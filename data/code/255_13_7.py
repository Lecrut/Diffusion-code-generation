def find_max_in_nested_list(nested_list):
    max_value = float('-inf')
    for element in nested_list:
        if isinstance(element, list):
            max_value = max(max_value, find_max_in_nested_list(element))
        else:
            max_value = max(max_value, element)
    return max_value
if __name__ == '__main__':
    sample_data = [1, 2, [3, 4, [5, 6], 7], 8]
    print(find_max_in_nested_list(sample_data))