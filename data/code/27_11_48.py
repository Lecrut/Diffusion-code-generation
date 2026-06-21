def values_differ(a, b):
    return a != b

if __name__ == '__main__':
    value1 = 3.14
    value2 = '3.14'
    print(values_differ(value1, value2))

    value3 = [1, 2, 3]
    value4 = [1, 2, 3]
    print(values_differ(value3, value4))

    value5 = {'key': 'value'}
    value6 = {'key': 'value'}
    print(values_differ(value5, value6))

    value7 = None
    value8 = False
    print(values_differ(value7, value8))