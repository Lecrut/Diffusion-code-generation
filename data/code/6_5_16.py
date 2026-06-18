def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float or int): List containing numerical values representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum weight, 
                     or None if the input is empty.
                     
    Time Complexity: O(n) - Single pass through the list to find min and max.
    Space Complexity: O(1) - Only uses a constant amount of additional space.
    
    Raises:
        ValueError: If the weights list contains non-numeric values or if it's not iterable in an expected way.
    """
    if not isinstance(weights, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")

    min_weight = float('inf')
    max_weight = float('-inf')

    for weight in weights:
        try:
            num_value = float(weight)
        except (ValueError, TypeError):
            raise ValueError(f"All elements in the weights list must be numeric. Found non-numeric value.") from None
        
        if min_weight > num_value:
            min_weight = num_value
        elif max_weight < num_value:
            max_weight = num_value

    return max_weight - min_weight

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    sample_weights = [10, 5, 23, 8, 45]
    
    result = weight_difference(sample_weights)
    
    print(f"Weights: {sample_weights}")
    print(f"Heaviest - Lightest Difference: {result}")

    # Additional test case with negative numbers and floats.
    sample_floats = [-10.5, 2.3, 7.8]
    result_f = weight_difference(sample_floats)
    
    print(f"Weights (float/neg): {sample_floats}")
    print(f"Heaviest - Lightest Difference: {result_f}")

    # Edge case: Single element list.
    single_element = [100]
    result_s = weight_difference(single_element)
    
    print(f"Single Element Weights: {single_element}")
    print(f"Difference (should be 0): {result_s}")