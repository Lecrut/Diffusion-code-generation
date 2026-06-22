def compare_values(value1, value2):
    def _compare_int_float(v1, v2):
        return v1 == v2

    def _compare_str(v1, v2):
        return v1.strip() == v2.strip()

    def _compare_list(v1, v2):
        if len(v1) != len(v2):
            return False
        for sub_v1, sub_v2 in zip(v1, v2):
            if not compare_values(sub_v1, sub_v2):
                return False
        return True

    def _compare_dict(v1, v2):
        if v1.keys() != v2.keys():
            return False
        for key in v1:
            if not compare_values(v1[key], v2[key]):
                return False
        return True

    comparison_map = {
        (int, int): _compare_int_float,
        (float, float): _compare_int_float,
        (str, str): _compare_str,
        (list, list): _compare_list,
        (dict, dict): _compare_dict,
    }

    type1, type2 = type(value1), type(value2)
    if (type1, type2) in comparison_map:
        return comparison_map[(type1, type2)](value1, value2)
    else:
        raise ValueError('Unsupported data types for comparison')

if __name__ == '__main__':
    print(compare_values(42, 42))
    print(compare_values(3.14, 3.14))
    print(compare_values(' hello ', 'hello'))
    print(compare_values([1, 2, 3], [1, 2, 3]))
    print(compare_values({'a': 1}, {'a': 1}))
    print(compare_values(42, '42'))