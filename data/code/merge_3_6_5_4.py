def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float/int): List containing numeric weight values.
        
    Returns:
        float or int: The difference between max and min weights, or None if empty.
    """
    if not weights:
        return None
    
    # Initialize with the first element to ensure O(n) single pass logic
    current_max = weights[0]
    current_min = weights[0]

    for weight in weights[1:]:
        if weight > current_max:
            current_max = weight
        elif weight < current_min:
            current_min = weight
            
    return current_max - current_min

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files)
    sample_weights = [85.0, 42.3, 91.5, 30.7, 85.0]
    
    result = weight_difference(sample_weights)
    
    print(f"Heaviest: {max(sample_weights)}")
    print(f"Lightest: {min(sample_weights)}")
    print(f"Difference: {result}")