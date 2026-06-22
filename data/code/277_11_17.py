def count_items(data):
    counts = {}
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 2, 'c': 3}
    result = count_items(sample_dict)
    print(result)

    sample_dict_empty = {}
    result_empty = count_items(sample_dict_empty)
    print(result_empty)

    sample_dict_with_duplicates = {'x': 1, 'y': 2, 'z': 2, 'x': 3}
    result_duplicates = count_items(sample_dict_with_duplicates)
    print(result_duplicates)