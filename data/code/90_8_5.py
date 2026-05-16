def simulate_boolean_logic(a, b, c, d):
    result = (a or b) or (c or d)
    return result
def test_boolean_logic(a, b, c, d, expected):
    actual = simulate_boolean_logic(a, b, c, d)
    if actual == expected:
        return True
    else:
        return False
if __name__ == '__main__':
    print("--- Simulation Tests ---")
    a1, b1, c1, d1 = False, False, False, False
    expected1 = False
    result1 = test_boolean_logic(a1, b1, c1, d1, expected1)
    print(f"Test 1 (F, F, F, F): Result={result1}, Expected={expected1}")
    a2, b2, c2, d2 = True, False, True, False
    expected2 = True
    result2 = test_boolean_logic(a2, b2, c2, d2, expected2)
    print(f"Test 2 (T, F, T, F): Result={result2}, Expected={expected2}")
    a3, b3, c3, d3 = True, True, True, True
    expected3 = True
    result3 = test_boolean_logic(a3, b3, c3, d3, expected3)
    print(f"Test 3 (T, T, T, T): Result={result3}, Expected={expected3}")
    a4, b4, c4, d4 = True, False, False, False
    expected4 = True
    result4 = test_boolean_logic(a4, b4, c4, d4, expected4)
    print(f"Test 4 (T, F, F, F): Result={result4}, Expected={expected4}")
    a5, b5, c5, d5 = False, False, True, False
    expected5 = True
    result5 = test_boolean_logic(a5, b5, c5, d5, expected5)
    print(f"Test 5 (F, F, T, F): Result={result5}, Expected={expected5}")
    a6, b6, c6, d6 = False, False, False, False
    expected6 = False
    result6 = test_boolean_logic(a6, b6, c6, d6, expected6)
    print(f"Test 6 (F, F, F, F): Result={result6}, Expected={expected6}")