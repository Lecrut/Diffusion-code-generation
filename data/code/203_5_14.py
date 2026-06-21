def compare_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both arguments must be dictionaries.")
    
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    
    if sum1 > sum2:
        return "dict1 is greater"
    elif sum1 < sum2:
        return "dict2 is greater"
    else:
        return "dictionaries are equal"

if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'x': 4, 'y': 5, 'z': 6}
    result = compare_dictionaries(dict1, dict2)
    print(result)