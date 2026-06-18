def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculates the absolute difference between two weight values.
    
    Args:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.
        
    Returns:
        float: The absolute difference between weight1 and weight2.
    """
    return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access
    sample_weight_1 = 50.75
    sample_weight_2 = 48.3
    
    result = calculate_weight_difference(sample_weight_1, sample_weight_2)
    
    print(f"The absolute difference between {sample_weight_1} and {sample_weight_2} is: {result}")