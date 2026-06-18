def calculate_weight_difference(w1: float | int, w2: float | int) -> float:
    """
    Calculate the absolute difference between two weight values.
    
    Args:
        w1 (float|int): First weight value.
        w2 (float|int): Second weight value.
        
    Returns:
        float: The absolute difference between w1 and w2.
    """
    return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_weights = [50.7, 48.3]
    
    result = calculate_weight_difference(sample_weights[0], sample_weights[1])
    print(f"Absolute difference: {result}")