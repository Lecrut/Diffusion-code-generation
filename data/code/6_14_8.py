def weight_range(weights):
    """
    Calculate the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float/int): List containing numerical weight values.
        
    Returns:
        float or int: The range (max - min) of the weights.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not weights:
        raise ValueError("Input list must not be empty.")

    # Using max() and min() on a generator expression avoids creating intermediate lists,
    # improving memory efficiency for very large datasets while maintaining readability.
    return float(max(weights)) - float(min(weights))

if __name__ == '__main__':
    sample_weights = [10.5, 23.4, 89.1, 12.7, 67.3]
    
    try:
        result = weight_range(sample_weights)
        print(f"Weight range (max - min): {result}")
    except ValueError as e:
        print(f"Error: {e}")