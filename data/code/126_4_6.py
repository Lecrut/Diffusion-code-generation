def yield_equality_check(a, b):
    if a == b:
        yield True
    else:
        yield False
if __name__ == '__main__':
    print("Test Case 1:")
    for result in yield_equality_check(10, 10):
        print(result)
    print("\nTest Case 2:")
    for result in yield_equality_check("hello", "hello"):
        print(result)
    print("\nTest Case 3:")
    for result in yield_equality_check(1, 2):
        print(result)
    print("\nTest Case 4:")
    for result in yield_equality_check([1, 2], [1, 2]):
        print(result)
    print("\nTest Case 5:")
    for result in yield_equality_check(None, None):
        print(result)
    print("\nTest Case 6:")
    for result in yield_equality_check(5.5, 5.500000000000001):
        print(result)