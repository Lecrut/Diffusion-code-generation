def calculate_weight_difference(x: float, y: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    Args:
        x (float): The first number.
        y (float): The second number.
        
    Returns:
        float: The absolute value of the difference (|x - y|).
    """
    return abs(x - y)

if __name__ == '__main__':
    sample_x = 10.5
    sample_y = 4.2
    
    result = calculate_weight_difference(sample_x, sample_y)
    
    # Direct output to demonstrate functionality without external input or files
    print(f"Absolute difference between {sample_x} and {sample_y}: {result}")