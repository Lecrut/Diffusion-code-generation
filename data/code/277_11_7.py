def count_items(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    
    counts = {}
    for key, value in data.items():
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    return counts

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'a': 3, 'c': 4}
    result = count_items(sample_dict)
    print(result)

    sample_dict_empty = {}
    result_empty = count_items(sample_dict_empty)
    print(result_empty)

    sample_dict_with_duplicates = {'x': 5, 'y': 6, 'x': 7}
    result_duplicates = count_items(sample_dict_with_duplicates)
    print(result_duplicates)