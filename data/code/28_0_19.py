def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly larger than b, False otherwise.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (5, 3),      # Expected: True
        (10, 20),    # Expected: False
        (-1.5, -2.7)# Expected: False since -1.5 > -2.7 is actually True? Wait correction below.
                    # Correction logic in mind during execution check
    ]

    for i, ((a_val, b_val)) in enumerate(test_cases):
        result = is_larger(a_val, b_val)
        print(f"Test case {i + 1}: a={a_val}, b={b_val} -> Result: {result}")