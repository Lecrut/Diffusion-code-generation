def are_types_equal(a, b):
    return type(a) is type(b)

def are_values_equal(a, b):
    try:
        return a == b
    except TypeError:
        return False

def are_equal(a, b):
    if not are_types_equal(a, b):
        return False
    return are_values_equal(a, b)

if __name__ == '__main__':
    print(f"Test 1 (Integers): {are_equal(10, 10)}")
    print(f"Test 2 (Floats): {are_equal(3.14, 3.14)}")
    print(f"Test 3 (Strings): {are_equal('hello', 'hello')}")
    print(f"Test 4 (Strings unequal): {are_equal('hello', 'world')}")
    print(f"Test 5 (Mixed types unequal): {are_equal(10, '10')}")
    print(f"Test 6 (Different types unequal): {are_equal(10, 10.0)}")
    print(f"Test 7 (Different types unequal): {are_equal([1], {1})}")