def are_values_equal(value1, value2):
    return value1 == value2

if __name__ == '__main__':
    print(are_values_equal('apple', 'apple'))
    print(are_values_equal(3.14, 3.14))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal({'key': 'value'}, {'key': 'value'}))