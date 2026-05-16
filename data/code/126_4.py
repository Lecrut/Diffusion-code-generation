def yield_equality_check(a, b):
    if a == b:
        yield True
    else:
        yield False
if __name__ == '__main__':
    print("Test Case 1 (Integers):")
    for result in yield_equality_check(10, 10):
        print(result)
    for result in yield_equality_check(10, 20):
        print(result)
    print("\nTest Case 2 (Strings):")
    for result in yield_equality_check("hello", "hello"):
        print(result)
    for result in yield_equality_check("hello", "world"):
        print(result)
    print("\nTest Case 3 (Lists):")
    for result in yield_equality_check([1, 2], [1, 2]):
        print(result)
    for result in yield_equality_check([1, 2], [2, 1]):
        print(result)
    print("\nTest Case 4 (Booleans):")
    for result in yield_equality_check(True, True):
        print(result)
    for result in yield_equality_check(True, False):
        print(result)
    print("\nTest Case 5 (Objects):")
    obj1 = [1, 2]
    obj2 = [1, 2]
    obj3 = [3, 4]
    for result in yield_equality_check(obj1, obj2):
        print(result)
    for result in yield_equality_check(obj1, obj3):
        print(result)