def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    This function uses Python's built-in abs() and subtraction operations,
    which are implemented in C for maximum efficiency at the interpreter level.
    
    Args:
        a (float): The first number.
        b (float): The second number.
        
    Returns:
        float: The absolute difference between a and b.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or files
    val1 = 3.50762849
    val2 = 1.23456789
    
    result = calculate_weight_difference(val1, val2)
    
    print(f"Absolute difference between {val1} and {val2}: {result}")