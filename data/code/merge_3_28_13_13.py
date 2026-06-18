def determine_larger(value1: float, value2: float) -> float:
    """
    Returns the larger of two comparable numeric values (integers or floats).
    
    Args:
        value1 (float): First numerical value.
        value2 (float): Second numerical value.
        
    Returns:
        float: The greater of the two input values.

    Raises:
        TypeError: If either argument is not a number (int, float, etc.).
    """
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    
    return value1 if value1 > value2 else value2

if __name__ == '__main__':
    # Sample test cases without any user input or external dependencies
    sample_cases = [
        ("Integers", 42, 30),
        ("Floats", 5.7, 6.2),
        ("Mixed Int/Float", -100, 10.9)
    ]

    for label, a, b in sample_cases:
        result = determine_larger(a, b)
        print(f"{label}: Larger value is {result}")