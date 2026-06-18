def compare_and_report(val1: float | int, val2: float | int) -> dict[str, float]:
    """
    Compares two numerical values and returns a dictionary with comparison details.
    
    Args:
        val1 (int or float): First arbitrary numerical value.
        val2 (int or float): Second arbitrary numerical value.
        
    Returns:
        dict: A dictionary containing 'larger', 'smaller', 'difference', 
              and 'ratio'. If values are equal, ratio is set to 1.0.
              
    Example:
        >>> compare_and_report(10, 5)
        {'larger': 10.0, 'smaller': 5.0, 'difference': 5.0, 'ratio': 2.0}
    """
    # Ensure both values are treated as floats for consistent arithmetic operations
    a = float(val1)
    b = float(val2)

    if abs(a - b) < 1e-9:  # Handle floating-point equality with tolerance
        return {
            'larger': a,
            'smaller': b,
            'difference': 0.0,
            'ratio': 1.0
        }

    larger = max(a, b)
    smaller = min(a, b)
    
    difference = abs(larger - smaller)
    ratio = larger / smaller if smaller != 0 else float('inf')

    return {
        'larger': larger,
        'smaller': smaller,
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10, 5),           # Simple integers
        (3.14, 2.71),     # Floats with difference
        (-5, -2),         # Negative numbers
        (0, 10),          # Zero as smaller value
        (1e-6, 1e-6),     # Very close floats (should return ratio 1.0)
    ]

    for i, (v1, v2) in enumerate(test_cases):
        result = compare_and_report(v1, v2)
        print(f"Test Case {i + 1}: Values ({v1}, {v2})")
        print(result)