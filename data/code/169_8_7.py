def validate_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both inputs must be dictionaries")

def subtract_counts(counts1, counts2):
    return {key: counts1.get(key, 0) - counts2.get(key, 0) for key in set(counts1) | set(counts2)}

def compare_item_counts(dict1=None, dict2=None):
    validate_dicts(dict1, dict2)
    if dict1 is None:
        dict1 = {}
    if dict2 is None:
        dict2 = {}
    return subtract_counts(dict1, dict2)

if __name__ == '__main__':
    sample_dict1 = {'apple': 3, 'banana': 5, 'cherry': 2}
    sample_dict2 = {'banana': 2, 'cherry': 4, 'date': 6}
    print(compare_item_counts(sample_dict1, sample_dict2))