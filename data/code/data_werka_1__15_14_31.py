def are_strictly_equal(value1, value2):
    return type(value1) is type(value2) and value1 == value2
if __name__ == '__main__':
    test_cases = [(5, 5), ('hello', 'hello'), (3.14, 3.14), ([1, 2, 3], [1, 2, 3]), ({'a': 1}, {'a': 1}), ((1, 2), (1, 2)), (True, True), (None, None), (5, '5'), ([1, 2], [2, 1])]
    for value1, value2 in test_cases:
        result = are_strictly_equal(value1, value2)
        print(f'are_strictly_equal({value1}, {value2}) -> {result}')