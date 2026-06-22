def are_strictly_equal(a, b):
    if a is None or b is None:
        return a is b
    else:
        return a is b and a == b
if __name__ == '__main__':
    sample1 = [1, 2, 3]
    sample2 = [1, 2, 3]
    sample3 = {'key': 'value'}
    sample4 = {'key': 'value'}
    sample5 = None
    sample6 = None
    print(are_strictly_equal(sample1, sample2))
    print(are_strictly_equal(sample3, sample4))
    print(are_strictly_equal(sample5, sample6))
    print(are_strictly_equal(10, 10))
    print(are_strictly_equal('test', 'test'))