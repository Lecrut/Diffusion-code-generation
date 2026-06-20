def are_values_equal(value1, value2):
    return value1 == value2
if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal('hello', 'hello'))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal({'a': 1}, {'a': 1}))
    print(are_values_equal(None, None))
    print(are_values_equal(5, '5'))
    print(are_values_equal([1, 2], [2, 1]))