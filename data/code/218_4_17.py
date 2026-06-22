def min_nested_list(nested_list):
    flat_list = [item for sublist in nested_list for item in (min_nested_list(sublist) if isinstance(item, list) else [item])]
    return min(flat_list)

if __name__ == '__main__':
    sample_data = [[3, 5], [1, 2], [4]]
    print(min_nested_list(sample_data))