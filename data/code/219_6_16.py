def flatten_and_find_max(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_and_find_max(item))
        else:
            flat_list.append(item)
    return max(flat_list)

if __name__ == '__main__':
    sample_list = [[1, 2, [3]], 4, [5, 6], 7]
    result = flatten_and_find_max(sample_list)
    print(result)