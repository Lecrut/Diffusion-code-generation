def are_equal(a, b):
    return type(a) == type(b) and a == b

if __name__ == '__main__':
    print(f"Test 1 (Integers): {are_equal(10, 10)}")
    print(f"Test 2 (Floats): {are_equal(3.14, 3.14)}")
    print(f"Test 3 (Strings): {are_equal('hello', 'hello')}")
    print(f"Test 4 (Strings unequal): {are_equal('hello', 'world')}")
    print(f"Test 5 (Mixed types unequal): {are_equal(10, '10')}")
    print(f"Test 6 (Different types unequal): {are_equal(10, 10.0)}")