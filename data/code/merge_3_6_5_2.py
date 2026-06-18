def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float/int): List containing numerical values representing weights.
        
    Returns:
        float or int: The difference between max and min weight, or None if input is empty/invalid.
    """
    if not isinstance(weights, list) or len(weights) == 0:
        return None
    
    try:
        # Find maximum value in O(n) time using built-in functions which are implemented efficiently in C
        max_weight = max(weights)
        min_weight = min(weights)
        
        return float(max_weight - min_weight) if isinstance(max_weight, int) else (max_weight - min_weight)
    except ValueError:
        # Handle cases where list contains non-numeric values
        return None

if __name__ == '__main__':
    sample_weights = [10.5, 23.4, 89.7, 5.2, 67.8]
    
    result = weight_difference(sample_weights)
    
    if result is not None:
        print(f"Heaviest: {max(sample_weights)}")
        print(f"Lightest: {min(sample_weights)}")
        print(f"Difference: {result}")
    else:
        print("Invalid input data.")