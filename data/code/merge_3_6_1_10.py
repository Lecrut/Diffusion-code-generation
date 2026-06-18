def calculate_weight_difference(a: float, b: float) -> float:
    """
    Returns the absolute difference between two floating-point numbers a and b.
    
    This implementation is efficient by directly using Python's built-in abs() 
    function which leverages C-level optimization for arithmetic operations.
    
    Args:
        a (float): The first number.
        b (float): The second number.
        
    Returns:
        float: The absolute value of the difference between a and b.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive input or files
    num1 = 5.7
    num2 = 3.4
    
    result = calculate_weight_difference(num1, num2)
    
    print(result)