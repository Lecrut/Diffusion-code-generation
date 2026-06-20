def are_equal(a, b):
    return a == b

if __name__ == '__main__':
    value1 = 3.14
    value2 = 3.14
    result = are_equal(value1, value2)
    print(result)

    value3 = 'world'
    value4 = 'WORLD'
    result = are_equal(value3, value4)
    print(result)

    value5 = [1, 2, 3]
    value6 = (1, 2, 3)
    result = are_equal(value5, value6)
    print(result)

    value7 = {'key': 'value'}
    value8 = {'key': 'Value'}
    result = are_equal(value7, value8)
    print(result)