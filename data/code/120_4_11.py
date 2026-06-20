def are_equal(val1, val2):
    if isinstance(val1, (int, float, str)):
        return val1 == val2
    elif isinstance(val1, list):
        if len(val1) != len(val2):
            return False
        for item1, item2 in zip(val1, val2):
            if not are_equal(item1, item2):
                return False
        return True
    elif isinstance(val1, dict):
        if len(val1) != len(val2):
            return False
        for key, value in val1.items():
            if key not in val2 or not are_equal(value, val2[key]):
                return False
        return True
    else:
        return id(val1) == id(val2)

if __name__ == '__main__':
    print(are_equal(5, 5))
    print(are_equal(5, 6))
    print(are_equal('hello', 'hello'))
    print(are_equal('hello', 'world'))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal([1, 2], [1, 3]))
    print(are_equal({'a': 1}, {'a': 1}))
    print(are_equal({'a': 1}, {'b': 1}))