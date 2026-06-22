def find_min_in_nested_list(nested_list):
    min_value = float('inf')
    for item in nested_list:
        if isinstance(item, list):
            sub_min = find_min_in_nested_list(item)
            if sub_min < min_value:
                min_value = sub_min
        elif item < min_value:
            min_value = item
    return min_value

if __name__ == '__main__':
    sample_data = [[3, 5], [1, 2], [4, [0, -1]]]
    print(find_min_in_nested_list(sample_data))