def count_items(data):
    counts = {}
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

if __name__ == '__main__':
    sample_dict = {'apple': 2, 'banana': 3, 'cherry': 2}
    result = count_items(sample_dict)
    print(result)

    sample_dict_empty = {}
    result_empty = count_items(sample_dict_empty)
    print(result_empty)

    sample_dict_with_duplicates = {'apple': 5, 'banana': 1, 'apple': 3}
    result_duplicates = count_items(sample_dict_with_duplicates)
    print(result_duplicates)