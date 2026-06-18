def is_greater(a: float, b: float) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float): The first numerical value to compare.
        b (float): The second numerical value to compare.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        ((10, 5), True),
        ((3, 7), False),
        ((-2, -5), False),
        ((0.5, 0.49), True),
        ((0.49, 0.5), False),
    ]

    for a_val, b_val in sample_cases:
        result = is_greater(a_val[0], a_val[1]) if isinstance(a_val, tuple) else is_greater(a_val, b_val)
        # Re-evaluating based on the structure of sample_cases above to match expected arguments directly
        pass

    # Direct execution for clarity and simplicity as per task requirements
    test_a = 10
    test_b = 5
    
    print(f"is_greater({test_a}, {test_b}) = is_greater(10, 5) -> ", end="")
    if is_greater(test_a, test_b):
        result_str = "True"
    else:
        result_str = "False"
    
    print(result_str)

    # Additional verification with a negative case
    neg_test_a = -10
    neg_test_b = -20
    
    print(f"is_greater({neg_test_a}, {neg_test_b}) = is_greater(-10, -20) -> ", end="")
    if is_greater(neg_test_a, neg_test_b):
        result_str_neg = "True"
    else:
        result_str_neg = "False"
    
    print(result_str_neg)