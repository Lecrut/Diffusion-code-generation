def compare_dicts(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    if sum1 > sum2:
        return "dict1 is greater"
    elif sum1 < sum2:
        return "dict2 is greater"
    else:
        return "dictionaries are equal"

if __name__ == '__main__':
    dict1 = {'a': 10, 'b': 20}
    dict2 = {'x': 5, 'y': 15, 'z': 5}
    result = compare_dicts(dict1, dict2)
    print(result)