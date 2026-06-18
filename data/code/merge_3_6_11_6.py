def calculate_weight_difference(w1: float, w2: float) -> float:
    """
    Calculates the absolute difference between two weight values.
    
    Args:
        w1 (float): First weight value.
        w2 (float): Second weight value.
        
    Returns:
        float: The absolute difference |w1 - w2|.
    """
    return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_w1 = 50.75
    sample_w2 = 48.3
    
    result = calculate_weight_difference(sample_w1, sample_w2)
    
    print(f"Weight difference: {result}")