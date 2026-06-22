def type_safe_compare(value1, value2):
    def _compare_numbers(v1, v2):
        return v1 == v2

    def _compare_strings(v1, v2):
        return v1.strip() == v2.strip()

    def _compare_lists(v1, v2):
        if len(v1) != len(v2):
            return False
        for sub_v1, sub_v2 in zip(v1, v2):
            if not type_safe_compare(sub_v1, sub_v2):
                return False
        return True

    def _compare_dicts(v1, v2):
        if v1.keys() != v2.keys():
            return False
        for key in v1:
            if not type_safe_compare(v1[key], v2[key]):
                return False
        return True

    type_to_comparator = {
        int: _compare_numbers,
        float: _compare_numbers,
        str: _compare_strings,
        list: _compare_lists,
        dict: _compare_dicts
    }

    type1, type2 = type(value1), type(value2)
    if type1 != type2:
        raise ValueError('Unsupported data types for comparison')
    
    if type1 not in type_to_comparator:
        raise ValueError('Unsupported data types for comparison')

    return type_to_comparator[type1](value1, value2)

if __name__ == '__main__':
    print(type_safe_compare(42, 42))
    print(type_safe_compare(3.14, 3.14))
    print(type_safe_compare(' hello ', 'hello'))
    print(type_safe_compare([1, 2, 3], [1, 2, 3]))
    print(type_safe_compare({'a': 1}, {'a': 1}))
    try:
        print(type_safe_compare(42, '42'))
    except ValueError as e:
        print(e)