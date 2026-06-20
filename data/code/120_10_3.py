def identity_and_type_safe_equal(a, b):
    return a is b or (type(a) == type(b) and a == b)
if __name__ == '__main__':
    print(identity_and_type_safe_equal(1, 1))
    print(identity_and_type_safe_equal(1, '1'))
    print(identity_and_type_safe_equal([1], [1]))
    print(identity_and_type_safe_equal([1], (1,)))