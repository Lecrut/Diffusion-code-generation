def weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A list containing numerical values representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum value.
                      Raises ValueError if the input is empty, None, or contains non-numeric types.
                      
    Complexity: O(n) time complexity for a single pass through the list.
    """
    if not weights:
        raise ValueError("Input list cannot be empty.")
        
    try:
        return max(weights) - min(weights)
    except TypeError as e:
        # Re-raise with more context about non-numeric types in specific cases, 
        # though the basic error message is sufficient for most scenarios.
        raise ValueError("All elements must be numeric.") from None

if __name__ == '__main__':
    sample_weights = [85.5, 72.0, 91.3, 68.4, 89.2]
    
    try:
        diff = weight_difference(sample_weights)
        print(f"Maximum Weight Difference for {sample_weights}:")
        print(f"Difference: {diff}")
    except ValueError as ve:
        print(f"Error calculation failed due to input issues: {ve}")