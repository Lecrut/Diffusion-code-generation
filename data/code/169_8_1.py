def compare_item_counts(dict1=None, dict2=None):
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
    sample_dict1 = {'apple': 3, 'banana': 5, 'cherry': 2}
    sample_dict2 = {'banana': 2, 'cherry': 4, 'date': 7}
    
    print(compare_item_counts(sample_dict1, sample_dict2))