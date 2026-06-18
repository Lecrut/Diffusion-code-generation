def calculate_weight_difference(w1: float, w2: float) -> float:
    """
    Calculate the absolute difference between two weight values.
    
    Args:
        w1 (float): The first weight value.
        w2 (float): The second weight value.
        
    Returns:
        float: The absolute difference |w1 - w2|.
    """
    return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    weight_a = 50.75
    weight_b = 49.30
    
    result = calculate_weight_difference(weight_a, weight_b)
    
    print(f"Weight A: {weight_a}")
    print(f"Weight B: {weight_b}")
    print(f"Absolute Difference: {result}")