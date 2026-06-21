ITEM_COUNT_MERGE_THRESHOLD = 1000

def merge_item_counts(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        if key in dict2:
            result[key] = value + dict2[key]
            del dict2[key]
        else:
            result[key] = value
    result.update(dict2)
    return result
if __name__ == '__main__':
    sample_dict1 = {'apple': 3, 'banana': 5}
    sample_dict2 = {'banana': 2, 'orange': 4}
    merged_result = merge_item_counts(sample_dict1, sample_dict2)
    print(merged_result)