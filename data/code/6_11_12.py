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
    w1 = 50.75
    w2 = 43.2
    
    result = calculate_weight_difference(w1, w2)
    
    print(f"The absolute difference between {w1} and {w2} is: {result}")