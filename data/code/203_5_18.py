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
    dict_a = {'apple': 5, 'banana': 3}
    dict_b = {'orange': 7, 'grape': 2}
    result = compare_dicts(dict_a, dict_b)
    print(result)