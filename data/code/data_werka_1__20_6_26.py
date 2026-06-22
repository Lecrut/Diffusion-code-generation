def deep_equal(obj1, obj2):
    if type(obj1) != type(obj2):
        return False
    if isinstance(obj1, dict):
        return all((deep_equal(obj1[key], obj2[key]) for key in obj1)) and all((key in obj2 for key in obj1))
    elif isinstance(obj1, list):
        return len(obj1) == len(obj2) and all((deep_equal(a, b) for a, b in zip(obj1, obj2)))
    else:
        return obj1 == obj2
if __name__ == '__main__':
    dict1 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    dict2 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    dict3 = {'a': 1, 'b': [2, 3], 'c': {'d': 5}}
    list1 = [1, [2, 3], {'d': 4}]
    list2 = [1, [2, 3], {'d': 4}]
    list3 = [1, [2, 3], {'d': 5}]
    print(deep_equal(dict1, dict2))
    print(deep_equal(dict1, dict3))
    print(deep_equal(list1, list2))
    print(deep_equal(list1, list3))