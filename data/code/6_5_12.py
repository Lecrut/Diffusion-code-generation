def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of int/float): List containing numerical values representing weights.
        
    Returns:
        float or None: The difference between max and min if valid input, else None.
    """
    if not weights:
        return None
    
    # Initialize with the first element to ensure O(n) single pass logic without sorting overhead
    current_min = weights[0]
    current_max = weights[0]

    for weight in weights[1:]:
        if weight < current_min:
            current_min = weight
        elif weight > current_max:
            current_max = weight
            
    return float(current_max - current_min)

if __name__ == '__main__':
    sample_weights = [5.0, 2.3, 8.1, 9.4, 3.7]
    
    result = weight_difference(sample_weights)
    print(f"Difference between heaviest and lightest: {result}")