def are_equal(a, b):
    if type(a) is type(b):
        return a == b
    return a == b
if __name__ == '__main__':
    print(f"Test 1 (Integers): {are_equal(10, 10)}")
    print(f"Test 2 (Floats): {are_equal(3.14, 3.14)}")
    print(f"Test 3 (Strings): {are_equal('hello', 'hello')}")
    print(f"Test 4 (Different types, equal value): {are_equal(10, 10.0)}")
    print(f"Test 5 (Different types, different value): {are_equal(10, 10.1)}")
    print(f"Test 6 (Different types, different value): {are_equal('a', 1)}")
    print(f"Test 7 (Different types, different value): {are_equal([1], {1})}")
    print(f"Test 8 (Different types, same type): {are_equal(True, True)}")
    print(f"Test 9 (Different types, same value): {are_equal(None, None)}")