def deep_equal(obj1, obj2):
    if type(obj1) != type(obj2):
        return False
    if isinstance(obj1, dict):
        if len(obj1) != len(obj2):
            return False
        for key in obj1:
            if key not in obj2 or not deep_equal(obj1[key], obj2[key]):
                return False
        return True
    elif isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        for item1, item2 in zip(obj1, obj2):
            if not deep_equal(item1, item2):
                return False
        return True
    else:
        return obj1 == obj2
if __name__ == '__main__':
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'a': 1, 'b': {'c': 2}}
    dict3 = {'a': 1, 'b': {'c': 3}}
    list1 = [1, [2, 3], 4]
    list2 = [1, [2, 3], 4]
    list3 = [1, [2, 4], 4]
    print(deep_equal(dict1, dict2))
    print(deep_equal(dict1, dict3))
    print(deep_equal(list1, list2))
    print(deep_equal(list1, list3))