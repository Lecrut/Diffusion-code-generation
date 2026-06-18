def calculate_weight_difference(weight_a: float, weight_b: float) -> float:
    """
    Calculate the absolute difference between two weight values.
    
    Args:
        weight_a (float): The first weight value.
        weight_b (float): The second weight value.
        
    Returns:
        float: The absolute difference between the two weights.
    """
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_weight_1 = 50.75
    sample_weight_2 = 48.3
    
    result = calculate_weight_difference(sample_weight_1, sample_weight_2)
    
    print(f"The absolute difference between {sample_weight_1} and {sample_weight_2} is: {result}")