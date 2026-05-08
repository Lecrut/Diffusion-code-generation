def yield_equality_check(a, b):
    if a == b:
        yield True
    else:
        yield False
if __name__ == '__main__':
    print("Test 1 (Integers):")
    for result in yield_equality_check(10, 10):
        print(result)
    for result in yield_equality_check(10, 20):
        print(result)
    print("\nTest 2 (Strings):")
    for result in yield_equality_check("hello", "hello"):
        print(result)
    for result in yield_equality_check("hello", "world"):
        print(result)
    print("\nTest 3 (Lists):")
    for result in yield_equality_check([1, 2], [1, 2]):
        print(result)
    for result in yield_equality_check([1, 2], [2, 1]):
        print(result)
    print("\nTest 4 (Booleans):")
    for result in yield_equality_check(True, True):
        print(result)
    for result in yield_equality_check(True, False):
        print(result)