def flatten_and_min(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_and_min(item))
        else:
            flat_list.append(item)
    return min(flat_list)
if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    print(flatten_and_min(sample_data))