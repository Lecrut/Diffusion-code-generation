def calculate_weight_difference(w1: float, w2: float) -> float:
    """
    Calculate the absolute difference between two weight values.
    
    Args:
        w1 (float): First weight value.
        w2 (float): Second weight value.
        
    Returns:
        float: The absolute difference |w1 - w2|.
    """
    return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    sample_weight_1 = 50.75
    sample_weight_2 = 48.3
    
    result = calculate_weight_difference(sample_weight_1, sample_weight_2)
    
    print(f"Absolute difference between {sample_weight_1} and {sample_weight_2}: {result}")