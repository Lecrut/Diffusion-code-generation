def safe_compare(value1, value2):
    if type(value1) != type(value2):
        return True
    if value1 is None or value2 is None:
        return value1 is not value2
    if isinstance(value1, (int, float, str)):
        return value1 != value2
    if isinstance(value1, list):
        return len(value1) != len(value2) or any((safe_compare(v1, v2) for v1, v2 in zip(value1, value2)))
    if isinstance(value1, dict):
        return value1.keys() != value2.keys() or any((safe_compare(value1[k], value2[k]) for k in value1))
    raise ValueError('Unsupported data type')
if __name__ == '__main__':
    print(safe_compare(10, 10))
    print(safe_compare(10, '10'))
    print(safe_compare(None, None))
    print(safe_compare(None, 0))
    print(safe_compare([1, 2], [1, 2]))
    print(safe_compare([1, 2], [2, 1]))
    print(safe_compare({'a': 1}, {'a': 1}))
    print(safe_compare({'a': 1}, {'b': 1}))