def lists_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if not identical(item1, item2):
            return False
    return True

def identical(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, list):
        return lists_identical(a, b)
    elif isinstance(a, dict):
        return dicts_identical(a, b)
    else:
        return a == b

def dicts_identical(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    for key in dict1:
        if key not in dict2 or not identical(dict1[key], dict2[key]):
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(lists_identical(list1, list2))
    list3 = [1, 2, 4]
    print(lists_identical(list1, list3))
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 2}}
    print(dicts_identical(dict1, dict2))
    dict3 = {'a': 1, 'b': {'c': 3}}
    print(dicts_identical(dict1, dict3))