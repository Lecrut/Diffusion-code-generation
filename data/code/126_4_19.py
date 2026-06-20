def check_equality(a, b):
    return type(a) == type(b) and a == b

if __name__ == '__main__':
    print("Test Case 1 (Integers):", check_equality(10, 10))
    print("Test Case 2 (Integers):", check_equality(10, 20))
    print("Test Case 3 (Strings):", check_equality("hello", "hello"))
    print("Test Case 4 (Strings):", check_equality("hello", "world"))
    print("Test Case 5 (Lists):", check_equality([1, 2], [1, 2]))
    print("Test Case 6 (Lists):", check_equality([1, 2], [2, 1]))