def flatten_and_min(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_and_min(item))
        else:
            flat_list.append(item)
    return min(flat_list)
if __name__ == '__main__':
    sample_data = [3, [5, 2], [8, [1, 9]], 4]
    print(flatten_and_min(sample_data))