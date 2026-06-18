def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float/int): List containing numerical values representing weights.
        
    Returns:
        float or int: The difference between maximum and minimum weight, or None if input is empty.
        
    Time Complexity: O(n) - Single pass through the list to find min and max.
    Space Complexity: O(1) - Only uses constant extra space for tracking min/max.
    """
    if not weights:
        return None
    
    # Initialize min_val with infinity, max_val with negative infinity
    min_val = float('inf')
    max_val = float('-inf')
    
    # Single pass to find both minimum and maximum values simultaneously
    for weight in weights:
        if weight < min_val:
            min_val = weight
        elif weight > max_val:
            max_val = weight
            
    return max_val - min_val

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_weights = [10.5, 23.7, 45.2, 8.9, 67.3]
    
    result = weight_difference(sample_weights)
    
    print(f"Weights: {sample_weights}")
    print(f"Heaviest - Lightest Difference: {result}")