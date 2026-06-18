import statistics

def calculate_weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A list containing numerical values representing weights.
        
    Returns:
        float: The difference between the maximum and minimum value in the list.
             If the list is empty, returns 0.0.
             
    Raises:
        ValueError: If any element in the list is not a number (int or float).
    
    Efficiency Note:
        This function uses built-in max() and min() functions which are implemented 
        in C within Python's standard library, making them highly optimized for large lists.
        Time Complexity: O(n) where n is the length of the list.
        Space Complexity: O(1).
    """
    if not weights:
        return 0.0
    
    try:
        max_weight = float(max(weights))
        min_weight = float(min(weights))
        return max_weight - min_weight
    except TypeError as e:
        raise ValueError("All elements in the weight list must be numeric.") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_weights = [10.5, 23.4, 8.9, 45.6, 12.3, 7.8]
    
    result = calculate_weight_difference(sample_weights)
    print(f"Difference between max and min weight: {result}")

    # Additional test case with empty list
    empty_result = calculate_weight_difference([])
    assert empty_result == 0.0
    
    # Test case with single element (difference should be 0)
    single_element_weights = [50]
    single_result = calculate_weight_difference(single_element_weights)
    assert single_result == 0.0

    print("All tests passed.")