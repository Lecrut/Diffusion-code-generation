def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    Args:
        a (float): First number.
        b (float): Second number.
        
    Returns:
        float: The absolute value of their difference.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 3.5
    val2 = 7.2
    
    result = calculate_weight_difference(val1, val2)
    
    print(f"The absolute difference between {val1} and {val2} is: {result}")