import math

def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers accurately 
    within standard IEEE 754 double-precision limits.

    Args:
        length1 (float): The numerator value.
        length2 (float): The denominator value.

    Returns:
        float: The quotient of length1 divided by length2, respecting 
              floating-point precision boundaries and handling division by zero gracefully.
    
    Raises:
        ZeroDivisionError: If length2 is exactly 0 or an underflow to 0 occurs during calculation.
    """
    # Use standard division which adheres to IEEE 754 for double-precision floats
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise TypeError("Both inputs must be numeric types compatible with Python's floating-point arithmetic.")

    result = length1 / length2
    
    # Check specifically for division by zero cases including potential underflow scenarios where the denominator becomes 0.0 after operations if it were dynamic (though here input is direct)
    if math.isinf(result):
        return float('nan')
    
    return result

if __name__ == '__main__':
    # Sample test values hard-coded to ensure no external dependencies or inputs are needed
    sample_l1 = 42.5
    sample_l2 = 8.0
    
    ratio_result = calculate_length_ratio(sample_l1, sample_l2)
    
    print(f"Ratio of {sample_l1} and {sample_l2}: {ratio_result}")