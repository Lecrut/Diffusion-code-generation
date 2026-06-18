def weight_range(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A non-empty list containing numerical values representing weights.
        
    Returns:
        float: The range (max - min) of the weights.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not weights:
        raise ValueError("The weight list cannot be empty.")

    # Using built-in max and min functions which are implemented in C for efficiency,
    # making this O(n) operation suitable for large lists compared to manual iteration loops.
    return float(max(weights)) - float(min(weights))

if __name__ == '__main__':
    sample_weights = [10.5, 23.4, 89.1, 5.6, 78.9]
    
    try:
        result = weight_range(sample_weights)
        print(f"Weight range for {sample_weights}: {result}")
    except ValueError as e:
        print(f"Error calculating weight range: {e}")