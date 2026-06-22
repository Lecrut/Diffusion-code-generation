def deep_equal(obj1, obj2):
    if type(obj1) != type(obj2):
        return False
    if isinstance(obj1, dict):
        if obj1.keys() != obj2.keys():
            return False
        for key in obj1:
            if not deep_equal(obj1[key], obj2[key]):
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
    sample_dict1 = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
    sample_dict2 = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
    sample_dict3 = {'a': 1, 'b': {'c': 2, 'd': [3, 5]}}
    print(deep_equal(sample_dict1, sample_dict2))
    print(deep_equal(sample_dict1, sample_dict3))
    sample_list1 = [1, 2, [3, 4]]
    sample_list2 = [1, 2, [3, 4]]
    sample_list3 = [1, 2, [3, 5]]
    print(deep_equal(sample_list1, sample_list2))
    print(deep_equal(sample_list1, sample_list3))