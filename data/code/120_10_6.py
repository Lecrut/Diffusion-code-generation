def identity_safe_equal(a, b):
    return a is b
if __name__ == '__main__':
    print(identity_safe_equal(1, 1))
    print(identity_safe_equal([1], [1]))
    print(identity_safe_equal(None, None))