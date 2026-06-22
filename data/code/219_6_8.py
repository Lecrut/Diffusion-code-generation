def flatten_and_find_max(nested_list):
    flat_list = [item for sublist in nested_list for item in (flatten_and_find_max(sublist) if isinstance(item, list) else [item])]
    return max(flat_list)

if __name__ == '__main__':
    sample_data = [[1, 2, [3]], 4, [5, [6, 7]]]
    print(flatten_and_find_max(sample_data))