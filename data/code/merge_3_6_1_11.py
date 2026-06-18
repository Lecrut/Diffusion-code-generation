def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    This function uses Python's built-in abs() and subtraction which are 
    implemented in C for maximum efficiency at the interpreter level.
    
    Args:
        a (float): First number.
        b (float): Second number.
        
    Returns:
        float: The absolute difference |a - b|.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    value1 = 3.5
    value2 = 7.2
    
    result = calculate_weight_difference(value1, value2)
    
    print(f"The absolute difference between {value1} and {value2} is: {result}")