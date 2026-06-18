import statistics

def calculate_weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A non-empty list containing numerical values representing weights.
        
    Returns:
        float: The difference between the maximum and minimum value in the list.
        
    Raises:
        ValueError: If the input list is empty.
        TypeError: If any element in the list is not a number.
    """
    if len(weights) == 0:
        raise ValueError("The weights list cannot be empty.")
    
    for weight in weights:
        if not isinstance(weight, (int, float)):
            raise TypeError(f"All elements must be numbers, got {type(weight).__name__}.")

    max_weight = max(weights)
    min_weight = min(weights)
    
    return max_weight - min_weight

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_weights_1 = [70.5, 68.2, 72.3, 69.8, 71.0]
    
    sample_weights_2 = [100, 200, 300, 400, 500]

    # Test case 1: Mixed decimal and integer weights
    result_1 = calculate_weight_difference(sample_weights_1)
    print(f"Difference for sample 1 (mixed decimals): {result_1}")

    # Test case 2: Integer weights with larger range
    result_2 = calculate_weight_difference(sample_weights_2)
    print(f"Difference for sample 2 (integers): {result_2}")
    
    # Verify correctness of results based on manual calculation
    assert abs(result_1 - 3.8) < 0.001, "Test case 1 failed"
    assert result_2 == 400, "Test case 2 failed"

    print("All tests passed.")