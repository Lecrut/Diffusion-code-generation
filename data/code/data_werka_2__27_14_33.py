def are_values_equal(value1, value2):
    if type(value1) != type(value2):
        return False
    if value1 is None or value2 is None:
        return value1 == value2
    if isinstance(value1, (int, float, str, bool)):
        return value1 == value2
    if isinstance(value1, list):
        return len(value1) == len(value2) and all((are_values_equal(v1, v2) for v1, v2 in zip(value1, value2)))
    if isinstance(value1, dict):
        return value1.keys() == value2.keys() and all((are_values_equal(value1[k], value2[k]) for k in value1))
    raise ValueError('Unsupported data type')
if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal(None, None))
    print(are_values_equal(None, 10))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal([1, 2], [2, 1]))
    print(are_values_equal({'a': 1}, {'a': 1}))
    print(are_values_equal({'a': 1}, {'b': 1}))