def calculate_weight_difference(w1: float, w2: float) -> float:
    """Calculate the absolute difference between two weight values."""
    return abs(w1 - w2)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    weight_a = 50.75
    weight_b = 43.20
    
    result = calculate_weight_difference(weight_a, weight_b)
    
    print(f"Weight Difference: {result}")