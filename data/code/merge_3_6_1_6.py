def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    This implementation uses Python's built-in abs() function which is 
    implemented in C and provides excellent performance for simple operations like this.
    
    Args:
        a (float): The first number.
        b (float): The second number.
        
    Returns:
        float: The absolute difference between the two numbers.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 10.5
    val2 = 4.7
    
    result = calculate_weight_difference(val1, val2)
    
    print(f"Absolute difference of {val1} and {val2}: {result}")