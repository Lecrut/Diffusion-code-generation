def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    This function uses Python's built-in abs() and subtraction operators,
    which are implemented in C for maximum efficiency at runtime.
    
    Parameters:
        a (float): First number.
        b (float): Second number.
        
    Returns:
        float: The absolute difference |a - b|.
    """
    return abs(a - b)

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 4.2
    
    result = calculate_weight_difference(sample_a, sample_b)
    
    print(f"Absolute difference of {sample_a} and {sample_b}: {result}")