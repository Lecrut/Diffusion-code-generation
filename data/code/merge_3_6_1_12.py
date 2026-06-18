def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.

    Parameters:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The absolute value of (a - b).
    
    Notes:
        This implementation uses Python's built-in abs() function, 
        which is implemented in C and provides optimal performance 
        for standard floating-point arithmetic operations.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    value1 = 45.6789
    value2 = 10.1234
    
    result = calculate_weight_difference(value1, value2)
    
    print(f"Absolute difference between {value1} and {value2}: {result}")