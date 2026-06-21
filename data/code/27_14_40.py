def safe_compare(value1, value2):
    if type(value1) != type(value2):
        return True
    if value1 is None or value2 is None:
        return value1 is not value2
    if isinstance(value1, (int, float, str)):
        return value1 != value2
    elif isinstance(value1, list):
        return _compare_lists(value1, value2)
    elif isinstance(value1, dict):
        return _compare_dicts(value1, value2)
    raise ValueError(f'Unsupported type: {type(value1)}')

def _compare_lists(list1, list2):
    if len(list1) != len(list2):
        return True
    for v1, v2 in zip(list1, list2):
        if safe_compare(v1, v2):
            return True
    return False

def _compare_dicts(dict1, dict2):
    if dict1.keys() != dict2.keys():
        return True
    for key in dict1:
        if safe_compare(dict1[key], dict2[key]):
            return True
    return False
if __name__ == '__main__':
    print(safe_compare(10, 20))
    print(safe_compare('hello', 'world'))
    print(safe_compare(None, None))
    print(safe_compare([1, 2], [1, 3]))
    print(safe_compare({'a': 1}, {'b': 1}))