def flatten_and_min(nested_list):
    flat_list = [item for sublist in nested_list for item in (flatten_and_min(sublist) if isinstance(item, list) else [item])]
    return min(flat_list)

if __name__ == '__main__':
    sample_data = [[3, 5], [1, 2], [4]]
    print(flatten_and_min(sample_data))