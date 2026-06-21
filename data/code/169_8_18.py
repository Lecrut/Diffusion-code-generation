def validate_input(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both inputs must be dictionaries.")
    return dict1, dict2

def compare_item_counts(dict1=None, dict2=None):
    dict1, dict2 = validate_input(dict1, dict2)
    result = {}
    for key in set(dict1) | set(dict2):
        count1 = dict1.get(key, 0)
        count2 = dict2.get(key, 0)
        result[key] = count1 - count2
    return result

if __name__ == '__main__':
    sample_dict1 = {'apple': 3, 'banana': 5, 'cherry': 2}
    sample_dict2 = {'banana': 2, 'cherry': 4, 'date': 7}
    print(compare_item_counts(sample_dict1, sample_dict2))