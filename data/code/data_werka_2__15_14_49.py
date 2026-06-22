def compare_values(value1, value2):
    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        return value1 == value2
    elif isinstance(value1, str) and isinstance(value2, str):
        return value1.strip() == value2.strip()
    elif isinstance(value1, list) and isinstance(value2, list):
        if len(value1) != len(value2):
            return False
        for item1, item2 in zip(value1, value2):
            if not compare_values(item1, item2):
                return False
        return True
    elif isinstance(value1, dict) and isinstance(value2, dict):
        if set(value1.keys()) != set(value2.keys()):
            return False
        for key in value1:
            if not compare_values(value1[key], value2[key]):
                return False
        return True
    else:
        raise ValueError('Unsupported data types for comparison')
if __name__ == '__main__':
    print(compare_values(42, 42))
    print(compare_values(3.14, 3.14))
    print(compare_values(' hello ', 'hello'))
    print(compare_values([1, 2, 3], [1, 2, 3]))
    print(compare_values({'a': 1, 'b': 2}, {'b': 2, 'a': 1}))
    print(compare_values(42, '42'))