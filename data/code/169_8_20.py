def compare_item_counts(dict1, dict2):
    if dict1 is None:
        dict1 = {}
    if dict2 is None:
        dict2 = {}

    result = {}
    for key in set(dict1) | set(dict2):
        count1 = dict1.get(key, 0)
        count2 = dict2.get(key, 0)
        result[key] = count1 - count2

    return result

if __name__ == '__main__':
    sample_dict1 = {'apple': 5, 'banana': 3}
    sample_dict2 = {'banana': 2, 'orange': 4}
    print(compare_item_counts(sample_dict1, sample_dict2))