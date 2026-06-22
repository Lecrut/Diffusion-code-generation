def find_min_in_nested_list(nested_list):
    min_val = float('inf')
    for item in nested_list:
        if isinstance(item, list):
            sub_min = find_min_in_nested_list(item)
            if sub_min < min_val:
                min_val = sub_min
        elif item < min_val:
            min_val = item
    return min_val

if __name__ == '__main__':
    sample_data = [[3, 5], [1, [2, 4]], 6]
    print(find_min_in_nested_list(sample_data))