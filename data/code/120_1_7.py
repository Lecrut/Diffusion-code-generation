def are_values_equal(value1, value2):
    if value1 is None and value2 is None:
        return True
    if value1 is None or value2 is None:
        return False
    return value1 == value2

if __name__ == '__main__':
    print(are_values_equal(42, 42))
    print(are_values_equal('hello', 'world'))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal({'a': 1}, {'a': 1}))
    print(are_values_equal(None, None))
    print(are_values_equal(None, 42))