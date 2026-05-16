if __name__ == '__main__':
    print("--- Testing Nested Boolean Expressions ---")
    test_cases = [
        (True, True, True, "Case 1: All True"),
        (True, False, True, "Case 2: Middle False"),
        (False, True, True, "Case 3: First False"),
        (False, False, True, "Case 4: First Two False"),
        (True, False, False, "Case 5: Last False"),
        (False, False, False, "Case 6: All False"),
        (True, True, False, "Case 7: Last False Only"),
        (False, True, False, "Case 8: Middle False Only"),
        (True, False, False, "Case 9: First False Only"),
        (False, False, False, "Case 10: All False (Recheck)"),
        (True, True, True, "Case 11: Boundary Check (All True)"),
        (True, False, True, "Case 12: Boundary Check (Mixed)"),
        (False, True, False, "Case 13: Boundary Check (Mixed)"),
    ]
    for a, b, c, description in test_cases:
        result = (a and b) or c
        status = "PASS" if result == (a and b) or c else "FAIL"
        print(f"{description}: a={a}, b={b}, c={c} -> Result: {result} ({status})")
    print("\n--- Testing Complex Nesting ---")
    complex_cases = [
        (True, (False and True), (True or False), "Complex Case A: True, False, True"),
        (False, (True and False), (False or False), "Complex Case B: False, False, False"),
        (True, (True and True), (True or True), "Complex Case C: True, True, True"),
        (False, (False and True), (False or True), "Complex Case D: False, False, True"),
    ]
    for a, b_expr, c_expr, description in complex_cases:
        result = a and b_expr or c_expr
        status = "PASS" if result == a and b_expr or c_expr else "FAIL"
        print(f"{description}: a={a}, b_expr={b_expr}, c_expr={c_expr} -> Result: {result} ({status})")