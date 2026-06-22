def flatten_and_find_max(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_and_find_max(item))
        else:
            flat_list.append(item)
    return max(flat_list)

if __name__ == '__main__':
    sample_data = [[3, 5, [2, 4]], [8], 10]
    result = flatten_and_find_max(sample_data)
    print(result)

    sample_data_2 = [[[1, 2], 3], 4, [5, [6, 7]]]
    result_2 = flatten_and_find_max(sample_data_2)
    print(result_2)

    sample_data_3 = [[-1, -2, [-3]], [-4, [-5, -6]], -7]
    result_3 = flatten_and_find_max(sample_data_3)
    print(result_3)