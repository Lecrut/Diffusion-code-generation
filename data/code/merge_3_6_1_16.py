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
    sample_a = 10.5
    sample_b = 3.2
    
    result = calculate_weight_difference(sample_a, sample_b)
    
    print(result)