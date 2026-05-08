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
    print("\nTest Case 4 (Objects):")
    obj1 = object()
    obj2 = object()
    obj3 = obj1
    print("obj1 == obj2:")
    for result in yield_equality_check(obj1, obj2):
        print(result)
    print("obj1 == obj3:")
    for result in yield_equality_check(obj1, obj3):
        print(result)