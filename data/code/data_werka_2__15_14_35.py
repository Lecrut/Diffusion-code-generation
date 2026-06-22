def type_safe_compare(value1, value2):
    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        return value1 == value2
    elif isinstance(value1, str) and isinstance(value2, str):
        return value1.strip() == value2.strip()
    elif isinstance(value1, list) and isinstance(value2, list):
        return len(value1) == len(value2) and all((type_safe_compare(v1, v2) for v1, v2 in zip(value1, value2)))
    elif isinstance(value1, dict) and isinstance(value2, dict):
        return value1.keys() == value2.keys() and all((type_safe_compare(value1[k], value2[k]) for k in value1))
    else:
        raise ValueError('Unsupported data types for comparison')
if __name__ == '__main__':
    print(type_safe_compare(42, 42))
    print(type_safe_compare(3.14, 3.14))
    print(type_safe_compare(' hello ', 'hello'))
    print(type_safe_compare([1, 2, 3], [1, 2, 3]))
    print(type_safe_compare({'a': 1}, {'a': 1}))
    print(type_safe_compare(42, '42'))