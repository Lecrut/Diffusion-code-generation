def calculate_weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float/int): List containing numerical weight values.
        
    Returns:
        float or int: The difference between maximum and minimum weight, 
                     or None if the list is empty.
                     
    Time Complexity: O(n) - Single pass through the list to find min and max.
    Space Complexity: O(1) - Only uses constant extra space for tracking min/max.
    """
    if not weights:
        return None
    
    # Initialize with first element
    current_min = float('inf')
    current_max = float('-inf')
    
    for weight in weights:
        if weight < current_min:
            current_min = weight
        elif weight > current_max:
            current_max = weight
            
    return current_max - current_min

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input needed)
    sample_weights = [10.5, 23.7, 8.9, 45.2, 6.1]
    
    result = calculate_weight_difference(sample_weights)
    
    print(f"Weights: {sample_weights}")
    if result is not None:
        print(f"Difference between heaviest and lightest weight: {result}")
    else:
        print("Error: Weight list cannot be empty.")