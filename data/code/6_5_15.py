def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float/int): List of numerical values representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum weight.
                      Raises ValueError if the input is empty.
                      
    Time Complexity: O(n) - Single pass through the list to find min and max.
    Space Complexity: O(1) - Constant extra space used for tracking min/max.
    """
    if not weights:
        raise ValueError("Input list cannot be empty.")

    # Initialize min_val with the first element, max_val also starts at the same value
    min_val = float('inf')  # Start with infinity to ensure any weight is smaller initially
    max_val = float('-inf') # Start with negative infinity to ensure any weight is larger initially
    
    for w in weights:
        if w < min_val:
            min_val = w
        elif w > max_val:
            max_val = w
            
    return max_val - min_val

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network)
    sample_weights = [85.5, 72.0, 91.3, 68.4, 85.5]

    result = weight_difference(sample_weights)
    
    print(f"Input weights: {sample_weights}")
    print(f"Heaviest - Lightest difference: {result}")