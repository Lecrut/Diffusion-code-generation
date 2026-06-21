def flatten_nested_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_nested_list(item))
        else:
            flat_list.append(item)
    return flat_list
if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(flatten_nested_list(sample_list))