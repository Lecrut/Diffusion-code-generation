def check_equality(a, b):
    if type(a) != type(b):
        return False
    return a == b

if __name__ == '__main__':
    print("Test Case 1 (Integers):")
    print(check_equality(10, 10))
    print(check_equality(10, 20))

    print("\nTest Case 2 (Strings):")
    print(check_equality("hello", "hello"))
    print(check_equality("hello", "world"))

    print("\nTest Case 3 (Lists):")
    print(check_equality([1, 2], [1, 2]))
    print(check_equality([1, 2], [2, 1]))