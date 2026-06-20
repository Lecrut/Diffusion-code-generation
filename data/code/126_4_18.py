def check_equality(a, b):
    try:
        return a == b
    except TypeError:
        return False

if __name__ == '__main__':
    result1 = check_equality(5, 5)
    print(f"Test Case 1 (Integers): {result1}")
    
    result2 = check_equality("python", "java")
    print(f"Test Case 2 (Strings): {result2}")
    
    result3 = check_equality([1, 2], [1, 2])
    print(f"Test Case 3 (Lists): {result3}")