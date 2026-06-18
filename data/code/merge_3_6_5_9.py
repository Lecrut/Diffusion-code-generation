def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float or int): List containing numerical values representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum value in the list.
                      Raises ValueError if the input is empty, None, or contains non-numeric types.
                      
    Time Complexity: O(n) - Single pass through the list to find min and max.
    Space Complexity: O(1) - Only uses constant extra space for tracking min/max.
    """
    if not weights:
        raise ValueError("Input list cannot be empty.")
    
    # Initialize with the first element
    current_min = float('inf')
    current_max = float('-inf')

    for weight in weights:
        try:
            num_weight = float(weight)  # Accepts both int and numeric types
        except (TypeError, ValueError):
            raise TypeError(f"All elements must be numeric. Got {type(weights[0])} at index.")
        
        if num_weight < current_min:
            current_min = num_weight
        elif num_weight > current_max:
            current_max = num_weight
            
    return round(current_max - current_min, 2)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    sample_weights = [10.5, 4.2, 8.9, 3.7, 12.1]

    try:
        result = weight_difference(sample_weights)
        print(f"Difference between heaviest and lightest weight: {result}")
    except Exception as e:
        print(f"Error occurred during calculation: {e}")