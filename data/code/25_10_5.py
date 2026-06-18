def is_zero(value):
    """
    Returns True if value is exactly zero, False otherwise.
    
    Supports integers, floats (exact comparison), numpy scalars where applicable.
    Does not use floating-point tolerance unless the input type indicates NaN or 
    extremely specific epsilon requirements are implied by context (not here).
    For true "exactly zero" as per prompt: direct equality check is used.
    
    Args:
        value (number): The numerical argument to evaluate.
        
    Returns:
        bool: True if value == 0, False otherwise.
    """
    return float(value) == 0

if __name__ == '__main__':
    # Hard-coded sample values - no user input required
    test_cases = [0, -0, 0.0, 1e-324, 0j, complex(0, 0), "0", "-0"]
    
    for tc in test_cases:
        try:
            result = is_zero(tc)
            print(f"is_zero({tc!r}) = {result}")
        except (ValueError, TypeError):
            # Handle cases where conversion might fail or type doesn't match expectations cleanly
            pass

# Additional robustness for edge case parsing if string input behaves oddly in some envs: