def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float or int): List of numerical values representing weights.
        
    Returns:
        float or None: The difference between max and min if valid, else None for empty input.
    """
    if not weights:
        return None
    
    # Initialize with the first element to ensure O(n) single pass logic without sorting overhead
    current_max = weights[0]
    current_min = weights[0]

    # Iterate through the rest of the list once
    for i in range(1, len(weights)):
        if weights[i] > current_max:
            current_max = weights[i]
        elif weights[i] < current_min:
            current_min = weights[i]

    return current_max - current_min

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_weights = [10.5, 23.4, 7.8, 99.1, 5.2]

    result = weight_difference(sample_weights)

    if result is not None:
        print(f"Heaviest - Lightest = {result}")
    else:
        print("No weights provided.")