def are_equal(item1, item2):
    return item1 == item2
if __name__ == '__main__':
    print(are_equal(42, 42))
    print(are_equal('hello', 'hello'))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal(3.14, 3.14))
    print(are_equal('world', 'hello'))
    print(are_equal([1, 2], [2, 1]))