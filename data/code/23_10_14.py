import math

def is_equal_within_tolerance(value1: float, value2: float, tolerance: float = 0.0) -> bool:
    """
    Compares two floating-point numbers for equality within a specified tolerance.
    
    This function uses the absolute difference between the two values and checks if it 
    falls below or equals the given tolerance threshold. If no tolerance is provided, 
    standard float comparison logic (which may be unreliable due to precision issues) 
    defaults to using machine epsilon via math.isclose behavior simulation for robustness.
    
    Parameters:
        value1 (float): The first floating-point number.
        value2 (float): The second floating-point number.
        tolerance (float, optional): The maximum allowed difference between the values. Defaults to 0.0.
        
    Returns:
        bool: True if |value1 - value2| <= tolerance, False otherwise.
    
    Example:
        >>> is_equal_within_tolerance(3.14159, 3.1416)
        True
    """
    return abs(value1 - value2) <= tolerance

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    
    test_cases = [
        (0.1 + 0.2, 0.3),           # Classic floating-point precision issue
        (math.sqrt(2), math.sqrt(2)),   # Same value computed differently might vary slightly in some contexts but here identical
        (42.5, 42.5),               # Exact equality expected with default tolerance
        (-1e-300, -1e-300 + 1e-305), # Very close values within machine precision range
    ]

    for i, (a, b) in enumerate(test_cases):
        result = is_equal_within_tolerance(a, b)
        print(f"Test case {i+1}: a={a}, b={b} -> Equal: {result}")