def are_conditions_mutually_exclusive(a, b, c):
    return (a + b + c) == 1

if __name__ == '__main__':
    result_1 = are_conditions_mutually_exclusive(True, False, True)
    print(f"Test Case 1 Result: {result_1}")
    
    result_2 = are_conditions_mutually_exclusive(False, False, False)
    print(f"Test Case 2 Result: {result_2}")
    
    result_3 = are_conditions_mutually_exclusive(True, True, False)
    print(f"Test Case 3 Result: {result_3}")