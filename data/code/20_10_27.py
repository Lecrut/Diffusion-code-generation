def are_objects_equal(x, y):
    return x == y
if __name__ == '__main__':
    print(are_objects_equal(42, 42))
    print(are_objects_equal('hello', 'hello'))
    print(are_objects_equal([1, 2, 3], [1, 2, 3]))
    print(are_objects_equal((1, 2), (2, 1)))
    print(are_objects_equal({'a': 1}, {'a': 1}))