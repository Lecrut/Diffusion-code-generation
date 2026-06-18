def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    Args:
        a (float): The first number.
        b (float): The second number.
        
    Returns:
        float: The absolute value of their difference.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any external input or files
    val1 = 250.75
    val2 = 89.34
    
    result = calculate_weight_difference(val1, val2)
    
    print(result)