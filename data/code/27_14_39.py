def safe_compare(value1, value2):
    if type(value1) != type(value2):
        return True
    if value1 is None or value2 is None:
        return value1 is not value2
    if isinstance(value1, (int, float, str)):
        return value1 != value2
    elif isinstance(value1, list):
        if len(value1) != len(value2):
            return True
        for v1, v2 in zip(value1, value2):
            if safe_compare(v1, v2):
                return True
        return False
    elif isinstance(value1, dict):
        key_diff = set(value1.keys()) ^ set(value2.keys())
        if key_diff:
            return True
        for key in value1:
            if safe_compare(value1[key], value2[key]):
                return True
        return False
    else:
        raise ValueError(f'Unsupported type: {type(value1)}')
if __name__ == '__main__':
    print(safe_compare(10, 20))
    print(safe_compare('hello', 'world'))
    print(safe_compare(None, None))
    print(safe_compare([1, 2], [1, 3]))
    print(safe_compare({'a': 1}, {'b': 2}))