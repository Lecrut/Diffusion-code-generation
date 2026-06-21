def safe_compare(value1, value2):
    if type(value1) != type(value2):
        return False
    if isinstance(value1, (int, float, str)):
        return value1 == value2
    elif isinstance(value1, list):
        return len(value1) == len(value2) and all((safe_compare(v1, v2) for v1, v2 in zip(value1, value2)))
    elif isinstance(value1, dict):
        return value1.keys() == value2.keys() and all((safe_compare(value1[k], value2[k]) for k in value1))
    else:
        raise ValueError(f'Unsupported type: {type(value1)}')
if __name__ == '__main__':
    print(safe_compare(5, 5))
    print(safe_compare(5.0, 5))
    print(safe_compare('hello', 'hello'))
    print(safe_compare([1, 2, 3], [1, 2, 3]))
    print(safe_compare([1, 2, 3], [1, 2, 4]))
    print(safe_compare({'a': 1, 'b': 2}, {'a': 1, 'b': 2}))
    print(safe_compare({'a': 1, 'b': 2}, {'a': 1, 'c': 2}))