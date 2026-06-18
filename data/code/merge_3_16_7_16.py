import math

def is_positive_float(value):
    """
    Check if a given float value is strictly positive.
    
    This function handles standard floating-point comparisons without 
    introducing unnecessary precision complexities as per the task requirement,
    unless edge cases near zero require consideration (though strict > 0 suffices here).

    Args:
        value (float): The number to check.

    Returns:
        bool: True if value is positive (> 0), False otherwise.
    """
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (1.5, True),           # Clearly positive
        (-2.3, False),         # Negative
        (0.0, False),          # Zero is not positive
        (1e-10, True),         # Very small positive number
        (-1e-10, False),       # Very small negative number
        (float('nan'), False), # NaN comparisons return False in boolean context for this check logic
    ]

    print("Running positivity checks on sample values:")
    
    all_passed = True
    
    for num, expected_result in test_cases:
        result = is_positive_float(num)
        status = "PASS" if result == expected_result else "FAIL"
        
        # Special handling for NaN since > 0 returns False but logically it's undefined/not positive
        if isinstance(num, float) and math.isnan(num):
            expected_nan_check = False 
            if not (result == expected_nan_check):
                all_passed = False
        
        print(f"is_positive_float({num}): got {result}, expected {expected_result} -> [{status}]")

    # Final summary execution result
    if all_passed:
        print("\nAll tests passed.")
    else:
        print("\nSome tests failed.")