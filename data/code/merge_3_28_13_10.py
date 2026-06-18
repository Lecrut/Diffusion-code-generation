def determine_larger(value1: float | int, value2: float | int) -> float | int:
    """
    Returns the larger of two comparable values (int or float).
    
    Args:
        value1: First numeric value.
        value2: Second numeric value.
        
    Returns:
        The greater of the two input values.
    """
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    
    return value1 if value1 > value2 else value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        ((5, 3), 5),           # Integers: larger is 5
        ((-10.5, -2.3), -2.3),# Floats: larger is -2.3 (closer to positive)
        ((42, 99), 99),        # Mixed logic check
        ((0, 0), 0),           # Equal values return either (condition returns first if equal due to > being False)
    ]

    for inputs in sample_cases:
        result = determine_larger(*inputs)
        expected = inputs[1]
        status = "PASS" if result == expected else f"FAIL (Expected {expected}, got {result})"
        print(f"{status} | Inputs: {inputs}")