def are_equal(item1, item2):
    return item1 == item2
if __name__ == '__main__':
    value1 = 42
    value2 = 42.0
    value3 = 'hello'
    value4 = [1, 2, 3]
    value5 = (1, 2, 3)
    print(are_equal(value1, value2))
    print(are_equal(value3, value3))
    print(are_equal(value4, value5))