def check_shared_keys(dict1: dict, dict2: dict) -> bool:
    return len(set(dict1.keys()) & set(dict2.keys())) > 0
if __name__ == '__main__':
    sample_dict_a = {'apple': 5, 'banana': 3}
    sample_dict_b = {'orange': 4, 'apple': 9}
    result = check_shared_keys(sample_dict_a, sample_dict_b)
    print(result)