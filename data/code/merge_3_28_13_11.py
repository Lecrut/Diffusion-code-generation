def determine_larger(value1: float | int, value2: float | int) -> float | int:
    """
    Returns the larger of two comparable values (int or float).
    
    Args:
        value1: The first numeric value.
        value2: The second numeric value.
        
    Returns:
        The greater of the two input values.
    """
    return max(value1, value2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (3, 7),           # Integers
        (-5.0, -2.0),    # Negative floats
        (42.1, 42.9),    # Floats close in value
        (int(float('inf')), float('-inf')) if hasattr(__builtins__, 'float') else None, 
    ]

    for i, case in enumerate(sample_cases):
        if case is not None:
            val1, val2 = case
            result = determine_larger(val1, val2)
            print(f"Case {i + 1}: Larger of ({val1}, {val2}) is {result}")