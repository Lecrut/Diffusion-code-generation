def deep_equal(obj1, obj2):

    def validate_and_compare(obj1, obj2):
        if type(obj1) != type(obj2):
            return False
        if isinstance(obj1, dict):
            return compare_dicts(obj1, obj2)
        elif isinstance(obj1, list):
            return compare_lists(obj1, obj2)
        else:
            return obj1 == obj2

    def compare_dicts(dict1, dict2):
        if len(dict1) != len(dict2):
            return False
        for key in dict1:
            if key not in dict2 or not validate_and_compare(dict1[key], dict2[key]):
                return False
        return True

    def compare_lists(list1, list2):
        if len(list1) != len(list2):
            return False
        for item1, item2 in zip(list1, list2):
            if not validate_and_compare(item1, item2):
                return False
        return True
    return validate_and_compare(obj1, obj2)
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    sample_dict2 = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    sample_dict3 = {'a': 1, 'b': [2, 3], 'c': {'d': 5}}
    sample_list1 = [1, 2, [3, 4]]
    sample_list2 = [1, 2, [3, 4]]
    sample_list3 = [1, 2, [3, 5]]
    print(deep_equal(sample_dict1, sample_dict2))
    print(deep_equal(sample_dict1, sample_dict3))
    print(deep_equal(sample_list1, sample_list2))
    print(deep_equal(sample_list1, sample_list3))