def type_safe_compare(value1, value2):
    def validate_and_compare(v1, v2, compare_func):
        if not isinstance(v1, type(v2)):
            raise ValueError('Unsupported data types for comparison')
        return compare_func(v1, v2)

    def compare_int_float(v1, v2):
        return v1 == v2

    def compare_str(v1, v2):
        return v1.strip() == v2.strip()

    def compare_list(v1, v2):
        if len(v1) != len(v2):
            return False
        for sub_v1, sub_v2 in zip(v1, v2):
            if not type_safe_compare(sub_v1, sub_v2):
                return False
        return True

    def compare_dict(v1, v2):
        if v1.keys() != v2.keys():
            return False
        for key in v1:
            if not type_safe_compare(v1[key], v2[key]):
                return False
        return True

    if isinstance(value1, (int, float)):
        return validate_and_compare(value1, value2, compare_int_float)
    elif isinstance(value1, str):
        return validate_and_compare(value1, value2, compare_str)
    elif isinstance(value1, list):
        return validate_and_compare(value1, value2, compare_list)
    elif isinstance(value1, dict):
        return validate_and_compare(value1, value2, compare_dict)
    else:
        raise ValueError('Unsupported data types for comparison')

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