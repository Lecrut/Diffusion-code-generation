if __name__ == '__main__':
    print("--- Testing Nested Boolean Expressions ---")
    test_cases = [
        (True, True, True, "Case 1: All True"),
        (True, False, True, "Case 2: Middle False"),
        (False, True, True, "Case 3: First False"),
        (False, False, True, "Case 4: First Two False"),
        (True, False, False, "Case 5: Last False"),
        (False, False, False, "Case 6: All False"),
        (True, True, False, "Case 7: Last False"),
        (False, True, False, "Case 8: Middle False"),
        (True, False, True, "Case 9: Mixed True/False"),
        (True, True, True, "Case 10: Boundary True"),
        (False, False, False, "Case 11: Boundary False"),
    ]
    for a, b, c, description in test_cases:
        result = (a and b) or c
        print(f"{description}: a={a}, b={b}, c={c} -> Result: {result}")
    print("\n--- Testing with specific boundary values ---")
    boundary_cases = [
        (True, True, True, "Boundary Test 1 (T, T, T)"),
        (True, True, False, "Boundary Test 2 (T, T, F)"),
        (True, False, True, "Boundary Test 3 (T, F, T)"),
        (False, True, True, "Boundary Test 4 (F, T, T)"),
        (False, False, True, "Boundary Test 5 (F, F, T)"),
        (True, False, False, "Boundary Test 6 (T, F, F)"),
    ]
    for a, b, c, description in boundary_cases:
        result = (a and b) or c
        print(f"{description}: a={a}, b={b}, c={c} -> Result: {result}")