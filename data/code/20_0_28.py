def are_equal(item1, item2):
    return item1 == item2
if __name__ == '__main__':
    print(are_equal(10, 10))
    print(are_equal('hello', 'hello'))
    print(are_equal([1, 2, 3], [1, 2, 3]))
    print(are_equal({'a': 1}, {'a': 1}))
    print(are_equal(10, '10'))
    print(are_equal((1, 2), [1, 2]))