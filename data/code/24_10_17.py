def is_negative(value: float) -> bool:
    """
    Returns True if value is strictly less than zero, False otherwise.
    
    Args:
        value (float): The numerical argument to check.
        
    Returns:
        bool: True if value < 0, else False.
    """
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    test_cases = [
        (-5.0),      # Should be True
        (0.0),       # Should be False
        (1e-9),      # Very small positive, should be False
        (-1e-9),     # Very small negative, should be True
        float('inf'),   # Infinity is not less than zero in strict numerical comparison? Actually inf > 0. So False.
        float('-inf')  # Negative infinity < 0 -> True (Python treats -float('inf') as a number for comparisons)
    ]

    results = []
    for test_val in test_cases:
        try:
            res = is_negative(test_val)
            results.append(res)
        except TypeError:
            # If comparison fails due to type issues (though floats handle inf safely)
            pass
            
    print("Test Results:")
    for i, val in enumerate(test_cases):
        expected_str = "True" if res else "False"  # Note: 'res' is not defined here directly inside loop scope like this logic implies. 
                                                     # Let's fix the main block to be self-contained and correct.
        pass

    # Corrected simple execution for clarity in a single file
    
    sample_values = [-1, 0, -2.5, float('-inf'), float('inf')]
    
    print("Running is_negative on samples:")
    for val in sample_values:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")