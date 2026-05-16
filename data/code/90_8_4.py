def simulate_boolean_logic(a, b, c, d, e):
    result = (a or b) or (c or d) or (e)
    return result
def test_boolean_logic(a, b, c, d, e, expected):
    actual = simulate_boolean_logic(a, b, c, d, e)
    if actual == expected:
        return True
    else:
        return False
if __name__ == '__main__':
    print("--- Simulation Tests ---")
    a1, b1, c1, d1, e1 = False, False, False, False, False
    expected1 = False
    result1 = test_boolean_logic(a1, b1, c1, d1, e1, expected1)
    print(f"Test 1 (F, F, F, F, F): Expected={expected1}, Actual={result1}")
    a2, b2, c2, d2, e2 = True, False, False, False, False
    expected2 = True
    result2 = test_boolean_logic(a2, b2, c2, d2, e2, expected2)
    print(f"Test 2 (T, F, F, F, F): Expected={expected2}, Actual={result2}")
    a3, b3, c3, d3, e3 = True, True, False, True, False
    expected3 = True
    result3 = test_boolean_logic(a3, b3, c3, d3, e3, expected3)
    print(f"Test 3 (T, T, F, T, F): Expected={expected3}, Actual={result3}")
    a4, b4, c4, d4, e4 = True, True, True, True, True
    expected4 = True
    result4 = test_boolean_logic(a4, b4, c4, d4, e4, expected4)
    print(f"Test 4 (T, T, T, T, T): Expected={expected4}, Actual={result4}")
    a5, b5, c5, d5, e5 = False, False, False, False, True
    expected5 = True
    result5 = test_boolean_logic(a5, b5, c5, d5, e5, expected5)
    print(f"Test 5 (F, F, F, F, T): Expected={expected5}, Actual={result5}")
    a6, b6, c6, d6, e6 = True, False, True, False, False
    expected6 = True
    result6 = test_boolean_logic(a6, b6, c6, d6, e6, expected6)
    print(f"Test 6 (T, F, T, F, F): Expected={expected6}, Actual={result6}")