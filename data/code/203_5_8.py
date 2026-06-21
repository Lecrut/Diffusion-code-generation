DICTIONARY_1 = {'a': 10, 'b': 20, 'c': 30}
DICTIONARY_2 = {'x': 5, 'y': 15, 'z': 25}

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
    result = compare_dictionaries(DICTIONARY_1, DICTIONARY_2)
    print(result)