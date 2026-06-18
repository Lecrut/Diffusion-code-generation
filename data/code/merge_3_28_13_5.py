def determine_larger(value1: float | int, value2: float | int) -> float | int:
    """
    Returns the larger of two comparable values (int or float).
    
    Args:
        value1: First numeric value.
        value2: Second numeric value.
        
    Returns:
        The greater of the two input values.
    """
    if isinstance(value1, int) and isinstance(value2, int):
        return max(int(value1), int(value2))
    elif isinstance(value1, float) or isinstance(value2, float):
        # Handle mixed types by converting to float for comparison logic, then cast back
        result = value1 if (value1 > value2 and not isinstance(value2, float)) else value2
        return max(float(value1), float(value2))
    else:
        raise TypeError("Both values must be integers or floats.")

if __name__ == '__main__':
    # Sample test cases without user input
    sample_cases = [
        (5, 3),           # Integers
        (-10.5, -2.3),   # Floats with negatives
        (42, 99),         # Simple integers
        (0.0, 0.0),       # Equal values
    ]

    for val1, val2 in sample_cases:
        result = determine_larger(val1, val2)
        print(f"Comparing {val1} and {val2}: Larger value is {result}")