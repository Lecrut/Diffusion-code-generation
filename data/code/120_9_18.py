def are_equal(a, b):
    return type(a) == type(b) and a == b

if __name__ == '__main__':
    value1 = 42
    value2 = "42"
    print(f"Test 1 (Integers unequal): {are_equal(value1, value2)}")
    
    value3 = 3.14
    value4 = 3.1400001
    print(f"Test 2 (Floats unequal): {are_equal(value3, value4)}")
    
    value5 = "hello"
    value6 = "world"
    print(f"Test 3 (Strings unequal): {are_equal(value5, value6)}")
    
    value7 = [1, 2, 3]
    value8 = [1, 2, 3]
    print(f"Test 4 (Lists equal): {are_equal(value7, value8)}")
    
    value9 = {"a": 1}
    value10 = {"a": 1}
    print(f"Test 5 (Dictionaries equal): {are_equal(value9, value10)}")