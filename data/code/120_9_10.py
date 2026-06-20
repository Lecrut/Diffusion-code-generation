def are_equal(a, b):
    if type(a) is not type(b):
        return False
    return a == b

if __name__ == '__main__':
    print(f"Test 1 (Integers): {are_equal(10, 10)}")
    print(f"Test 2 (Floats): {are_equal(3.14, 3.14)}")
    print(f"Test 3 (Strings): {are_equal('hello', 'hello')}")
    print(f"Test 4 (Different Types, Equal Value): {are_equal(10, 10.0)}")
    print(f"Test 5 (Different Types, Unequal Value): {are_equal(10, 10.1)}")
    print(f"Test 6 (Different Types, Unequal Type): {are_equal('a', 1)}")
    print(f"Test 7 (Different Types, Unequal Type): {are_equal([1], {1})}")
    print(f"Test 8 (None and False): {are_equal(None, False)}")