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
    # Hard-coded sample values for testing without user input or external dependencies
    val_a = 50.75
    val_b = 32.4
    
    result = calculate_weight_difference(val_a, val_b)
    
    print(f"Absolute difference between {val_a} and {val_b}: {result}")