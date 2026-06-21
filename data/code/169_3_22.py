def merge_item_counts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
if __name__ == '__main__':
    sample_dict1 = {'apple': 3, 'banana': 5}
    sample_dict2 = {'banana': 2, 'cherry': 7}
    merged_dict = merge_item_counts(sample_dict1, sample_dict2)
    print(merged_dict)