def identity_and_type_safe_equal(a, b):
    if type(a) is not type(b):
        return False
    return a is b or a == b
if __name__ == '__main__':
    value1 = 42
    value2 = 42
    value3 = 'hello'
    value4 = 'world'
    print(identity_and_type_safe_equal(value1, value2))
    print(identity_and_type_safe_equal(value1, value3))
    print(identity_and_type_safe_equal(value3, value4))