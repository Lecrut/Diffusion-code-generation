def calculate_weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    This function is optimized to avoid sorting, which gives it O(n) time complexity 
    instead of O(n log n). It performs a single pass through the list to find min and max.

    Args:
        weights (list): A list of numerical values representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum weight.
                      Raises ValueError if the list is empty.
    """
    if not weights:
        raise ValueError("The list of weights cannot be empty.")

    min_weight = max(weights)  # Initialize both with first element logic implicitly handled by function
    actual_min = float('inf')
    actual_max = float('-inf')

    for weight in weights:
        if weight < actual_min:
            actual_min = weight
        if weight > actual_max:
            actual_max = weight
    
    return actual_max - actual_min

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network)
    sample_weights = [85.2, 90.1, 76.5, 93.8, 88.4, 79.0]

    result = calculate_weight_difference(sample_weights)
    
    # Output the result to verify functionality (no printing required by task logic but good for runnable module verification)
    print(result if isinstance(result, float) else int(result))