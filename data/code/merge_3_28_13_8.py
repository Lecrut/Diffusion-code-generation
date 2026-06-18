def determine_larger(value1: float | int, value2: float | int) -> float | int:
    """
    Returns the larger of two comparable values (int or float).
    
    Args:
        value1: First numeric value.
        value2: Second numeric value.
        
    Returns:
        The greater value between value1 and value2.
    """
    if value1 > value2:
        return value1
    else:
        return value2

if __name__ == '__main__':
    # Sample test cases with various comparable data types
    sample_cases = [
        (5, 3),            # Integers
        (5.5, 6),          # Floats and int mix
        (-10, -4),         # Negative integers
        (2.79e-3, 3e-3),   # Small floating point numbers in scientific notation
    ]

    for val1, val2 in sample_cases:
        result = determine_larger(val1, val2)
        print(f"Comparing {val1} and {val2}: Larger is {result}")