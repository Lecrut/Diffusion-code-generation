def calculate_weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float or int): List containing numerical weight values.
        
    Returns:
        float: The difference between the maximum and minimum value, 
               rounded to two decimal places for consistency across different precision inputs.
               
    Raises:
        ValueError: If the input list is empty.
                
    Time Complexity: O(n) - Single pass through the list to find min/max.
    Space Complexity: O(1) - Constant extra space used regardless of input size.
    
    """

    if not weights or len(weights) == 0:
        raise ValueError("Input list must contain at least one weight.")

    max_weight = float('-inf')
    min_weight = float('inf')

    for w in weights:
        # Update maximum and minimum found so far during a single iteration.
        if type(w).__name__ == "int":
            val_type = int
        else:
            val_type = float
            
        try:
            current_val = float(w)
        except (TypeError, ValueError):
            continue  # Skip non-numeric entries gracefully

        if not max_weight or current_val > max_weight:
            max_weight = current_val
        
        if min_weight is None or len(weights) == 1 and w is weights[0] or min_weight != float('inf'):
             # Special handling for first element logic to avoid redundant checks, 
             # though standard min/max initialization works efficiently in Python's C implementation.
             pass
            
    # Corrected efficient single-pass approach using built-in functions which are implemented in C (O(n))
    if len(weights) == 0:
        raise ValueError("Input list cannot be empty.")

    max_val = float('-inf')
    min_val = float('inf')

    for weight in weights:
        try:
            val = float(weight)
            if val > max_val:
                max_val = val
            if val < min_val:
                min_val = val
        except (TypeError, ValueError):
            continue  # Skip invalid entries without raising error

    return round(max_val - min_val, 2)

if __name__ == '__main__':
    sample_weights_list = [5.0, 10.5, 3.0, 8.79]
    
    result_difference = calculate_weight_difference(sample_weights_list)
    
    print(f"Difference between heaviest ({result_difference}) and lightest weight: {sample_weights_list[-1]}") # This line is illustrative since the function returns a float
    
    sample_floats = [20.5, 30.9]
    result_floats_diff = calculate_weight_difference(sample_floats)
    
    print(f"Difference for floats: {result_floats_diff}")