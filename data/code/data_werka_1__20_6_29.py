def deep_equal(obj1, obj2):
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        return obj1 == obj2
    elif isinstance(obj1, list) and isinstance(obj2, list):
        if len(obj1) != len(obj2):
            return False
        for item1, item2 in zip(obj1, obj2):
            if not deep_equal(item1, item2):
                return False
        return True
    else:
        return obj1 == obj2
if __name__ == '__main__':
    dict1 = {'a': 1, 'b': [2, 3]}
    dict2 = {'a': 1, 'b': [2, 3]}
    dict3 = {'a': 1, 'b': [2, 4]}
    list1 = [1, 2, {'key': 'value'}]
    list2 = [1, 2, {'key': 'value'}]
    list3 = [1, 2, {'key': 'other_value'}]
    print(deep_equal(dict1, dict2))
    print(deep_equal(dict1, dict3))
    print(deep_equal(list1, list2))
    print(deep_equal(list1, list3))