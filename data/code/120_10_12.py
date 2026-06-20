def identity_and_type_safe_equal(a, b):
    if type(a) is not type(b):
        return False
    return a is b
if __name__ == '__main__':
    print(identity_and_type_safe_equal(1, 1))
    print(identity_and_type_safe_equal(1, 2))
    print(identity_and_type_safe_equal('a', 'a'))
    print(identity_and_type_safe_equal('a', 'b'))
    print(identity_and_type_safe_equal([1], [1]))
    print(identity_and_type_safe_equal([], []))