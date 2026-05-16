def are_equal(a, b):
    if type(a) != type(b):
        return False
    if a == b:
        return True
    return False
if __name__ == '__main__':
    print(f"Test 1 (Integers): {are_equal(10, 10)}")
    print(f"Test 2 (Floats): {are_equal(3.14, 3.14)}")
    print(f"Test 3 (Strings): {are_equal('hello', 'hello')}")
    print(f"Test 4 (Strings unequal): {are_equal('hello', 'world')}")
    print(f"Test 5 (Mixed types unequal): {are_equal(10, '10')}")
    print(f"Test 6 (Different types): {are_equal(10, 10.0)}")
    print(f"Test 7 (Different types unequal): {are_equal([1], {1})}")