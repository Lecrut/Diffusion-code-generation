def simulate_boolean_logic(a, b, c, d):
    result = (a or b) or (c or d)
    return result
def test_boolean_logic(a, b, c, d, expected):
    actual = simulate_boolean_logic(a, b, c, d)
    assert actual == expected, f"Test failed for a={a}, b={b}, c={c}, d={d}. Expected: {expected}, Got: {actual}"
    return True
if __name__ == '__main__':
    print("Starting Boolean Logic Simulation and Testing")
    a1, b1, c1, d1 = False, False, False, False
    expected1 = False
    test_boolean_logic(a1, b1, c1, d1, expected1)
    print(f"Test Case 1 Passed: Result = {simulate_boolean_logic(a1, b1, c1, d1)}")
    a2, b2, c2, d2 = True, False, False, True
    expected2 = True
    test_boolean_logic(a2, b2, c2, d2, expected2)
    print(f"Test Case 2 Passed: Result = {simulate_boolean_logic(a2, b2, c2, d2)}")
    a3, b3, c3, d3 = True, True, True, True
    expected3 = True
    test_boolean_logic(a3, b3, c3, d3, expected3)
    print(f"Test Case 3 Passed: Result = {simulate_boolean_logic(a3, b3, c3, d3)}")
    a4, b4, c4, d4 = True, True, False, False
    expected4 = True
    test_boolean_logic(a4, b4, c4, d4, expected4)
    print(f"Test Case 4 Passed: Result = {simulate_boolean_logic(a4, b4, c4, d4)}")
    a5, b5, c5, d5 = False, False, True, False
    expected5 = True
    test_boolean_logic(a5, b5, c5, d5, expected5)
    print(f"Test Case 5 Passed: Result = {simulate_boolean_logic(a5, b5, c5, d5)}")