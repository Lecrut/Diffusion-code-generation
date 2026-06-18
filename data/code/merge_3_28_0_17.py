def is_larger(a: float | int, b: float | int) -> bool:
    """
    Returns True if a is strictly larger than b, otherwise False.
    
    Args:
        a (float|int): The first number to compare.
        b (float|int): The second number to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases running without any user input or external dependencies
    sample_cases = [
        (5, 3),      # Expected: True
        (10, 10),    # Expected: False (equal)
        (-2, -5),    # Expected: True
        ("a", "b"),  # This will raise a TypeError as expected for non-numeric inputs in comparison contexts if strictly typed, but Python allows string comparison. For numeric robustness we assume valid input per task description of 'numbers'. Adjusted to integers only for safety demonstration below.
    ]

    print("Running sample tests...")
    
    # Re-defining cases with explicit numbers to ensure type correctness as per "two numbers" requirement
    test_data = [
        (5, 3),       # True
        (10, 10),     # False
        (-2.5, -5.0), # True
        (float('inf'), float('-inf')), # True
        (0, 0),       # False
    ]

    for a_val, b_val in test_data:
        result = is_larger(a_val, b_val)
        print(f"is_larger({a_val}, {b_val}) => {result}")