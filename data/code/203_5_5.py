def compare_dictionaries(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    if sum1 > sum2:
        return "dict1 is greater"
    elif sum1 < sum2:
        return "dict2 is greater"
    else:
        return "dictionaries are equal"

if __name__ == '__main__':
    dict1 = {'apple': 10, 'banana': 5}
    dict2 = {'orange': 8, 'grape': 7}
    result = compare_dictionaries(dict1, dict2)
    print(result)