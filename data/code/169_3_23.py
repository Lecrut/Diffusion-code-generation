def merge_item_counts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both arguments must be dictionaries.")
    
    result = dict1.copy()
    for key, value in dict2.items():
        if not isinstance(key, str) or not isinstance(value, (int, float)):
            raise ValueError("Keys must be strings and values must be numbers.")
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

if __name__ == '__main__':
    sample_dict1 = {'apple': 3, 'banana': 5}
    sample_dict2 = {'banana': 2, 'orange': 4}
    merged_result = merge_item_counts(sample_dict1, sample_dict2)
    print(merged_result)