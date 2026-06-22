def flatten_and_find_min(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_and_find_min(item))
        else:
            flat_list.append(item)
    return min(flat_list)
if __name__ == '__main__':
    sample_data = [3, [5, 2], [[1, 4], 6], 7]
    print(flatten_and_find_min(sample_data))