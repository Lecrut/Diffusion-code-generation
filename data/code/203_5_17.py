def compare_dict_sums(dict1, dict2):
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
    print(compare_dict_sums(dict1, dict2))