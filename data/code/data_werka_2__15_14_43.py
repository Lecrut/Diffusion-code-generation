def type_safe_compare(value1, value2):
    comparison_map = {(int, int): lambda x, y: x == y, (float, float): lambda x, y: x == y, (str, str): lambda x, y: x.strip() == y.strip(), (list, list): lambda x, y: len(x) == len(y) and all((type_safe_compare(v1, v2) for v1, v2 in zip(x, y))), (dict, dict): lambda x, y: x.keys() == y.keys() and all((type_safe_compare(x[k], y[k]) for k in x))}
    type_pair = (type(value1), type(value2))
    if type_pair in comparison_map:
        return comparison_map[type_pair](value1, value2)
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