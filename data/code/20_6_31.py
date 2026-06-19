def deep_equals(obj1, obj2):
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        return all((key in obj2 and deep_equals(obj1[key], obj2[key]) for key in obj1))
    elif isinstance(obj1, list) and isinstance(obj2, list):
        return len(obj1) == len(obj2) and all((deep_equals(item1, item2) for item1, item2 in zip(obj1, obj2)))
    else:
        return obj1 == obj2
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
    sample_dict2 = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
    sample_dict3 = {'a': 1, 'b': {'c': 2, 'd': [3, 5]}}
    sample_list1 = [1, 2, [3, 4]]
    sample_list2 = [1, 2, [3, 4]]
    sample_list3 = [1, 2, [3, 5]]
    print(deep_equals(sample_dict1, sample_dict2))
    print(deep_equals(sample_dict1, sample_dict3))
    print(deep_equals(sample_list1, sample_list2))
    print(deep_equals(sample_list1, sample_list3))