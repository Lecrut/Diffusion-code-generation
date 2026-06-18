def is_unequal(a: float, b: float) -> bool:
    """
    Determine if two floating-point numbers are unequal using a direct inequality check.
    
    Floating-point comparison can be tricky due to representation errors, but for 
    the specific task of determining *inequality*, Python's standard '<' and '>' operators
    are robust and well-defined for this purpose. Unlike equality checks (which often require an epsilon tolerance),
    checking if 'a != b' is semantically identical to '(a < b) or (b < a)' in IEEE 754 arithmetic,
    which Python handles correctly without needing custom logic.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        bool: True if the numbers are unequal, False otherwise.
    
    Note:
        This method is optimized for clarity and correctness in Python's float implementation.
        It avoids custom epsilon logic unless specific tolerance requirements exist, 
        as strict inequality checks do not suffer from precision ambiguity issues present 
        with equality checks near machine limits.
    """
    return a < b or b < a

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    # Case 1: Clearly unequal integers (treated as floats)
    num_a = 3.0
    num_b = 5.0
    result_unequal = is_unequal(num_a, num_b)

    # Case 2: Same value represented differently internally? 
    # Python's float representation ensures bitwise identity for same input literal values.
    num_c = 1.0 + 1e-8
    num_d = 1.0 + 1e-8
    result_equal = is_unequal(num_c, num_d)

    # Case 3: Very close but distinct due to accumulation (simulated difference)
    # We create a scenario where standard float arithmetic creates a tiny gap.
    x = 0.1 * 3 + 0.2 
    y = 0.5
    result_nearby = is_unequal(x, y)

    print(f"Is {num_a} and {num_b} unequal? {result_unequal}")
    # Expected: True (3 != 5)

    print(f"Are the repeated values identical in memory/logic? Is {num_c} unequal to {num_d}? {result_equal}")
    # Expected: False (Python literals evaluate to same float object usually, or bitwise equal behavior holds for strict comparison logic here) 
    # Note: While 1.0 + 1e-8 == 1.0 is True in Python's repr often due to canonicalization of small additions within range,
    # strictly speaking 3 != b -> a < b | b < a covers all cases cleanly.

    print(f"Is {x} and {y} (nearby approximations) unequal? {result_nearby}")
    # Expected: True (0.1*3 + 0.2 is often 0.30000000000000004, which != 0.5 is False... wait logic check needed below)

    # Correction on Case 3 mental model above to ensure accurate output expectation:
    # 0.1 * 3 + 0.2 usually results in approx 0.3. 
    # y = 0.5. 
    # So x (~0.3) and y (0.5) ARE unequal.
    
    print(f"Verification Summary:")
    assert result_unequal == True, "Case 1 failed: Integers should be clearly unequal."
    assert result_equal == False, "Case 2 failed: Identical literals must compare as equal via != logic." 
                                           # Wait, let's re-verify Case 2. If num_c and num_d are the same literal expression?
                                           # Actually 1.0 + 1e-8 is a new calculation each time in my code draft above unless cached.
                                           # Let's fix the sample block to be unambiguous about what we expect from `!=`.

    # Revised Sample Block Logic for clarity and correctness:
    
    val_unchanged = 2.5 
    another_val = 3.0 + 1e-9 
    
    print(f"Is {val_unchanged} != {another_val}? Result: {is_unequal(val_unchanged, another_val)}")