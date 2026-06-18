def compare_lengths(a: float, b: float) -> tuple[float, str]:
    """
    Computes the absolute difference between two floating-point numbers
    and returns a string indicating which number is greater (if different).
    
    Args:
        a: First floating-point number.
        b: Second floating-point number.
        
    Returns:
        A tuple containing:
            - The absolute difference between a and b as a float.
            - A descriptive string stating the relationship between their magnitudes.
    """
    diff = abs(a - b)
    
    if a > b:
        result_str = f"{a} is greater than {b}"
    elif b > a:
        result_str = f"{b} is greater than {a}"
    else:
        result_str = "Both lengths are equal"
        
    return diff, result_str

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 3.14159
    val2 = 2.71828
    
    difference, description = compare_lengths(val1, val2)
    
    print(f"Absolute Difference: {difference}")
    print(f"Comparison Result: {description}")