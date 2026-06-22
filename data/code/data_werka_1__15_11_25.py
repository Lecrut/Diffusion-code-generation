def are_objects_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(are_objects_equal(10, 10))  # True
    print(are_objects_equal('hello', 'world'))  # False
    print(are_objects_equal([1, 2, 3], [1, 2, 3]))  # True
    print(are_objects_equal({'a': 1}, {'a': 1}))  # True