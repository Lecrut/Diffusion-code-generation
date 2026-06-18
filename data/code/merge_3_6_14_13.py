def weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float/int): A non-empty list of numerical values representing weights.
        
    Returns:
        float: The difference between the maximum and minimum value in the list.
        Raises:
            ValueError: If the input list is empty or None.
            
    Efficiency Note:
        Uses a single pass to find min and max, achieving O(n) time complexity 
        and O(1) space complexity. This is optimal for large lists compared to sorting-based approaches (O(n log n)).
    """
    if not weights:
        raise ValueError("The list of weights cannot be empty.")

    maximum = float('-inf')
    minimum = float('inf')

    for weight in weights:
        if weight > maximum:
            maximum = weight
        if weight < minimum:
            minimum = weight
            
    return maximum - minimum

if __name__ == '__main__':
    sample_weights = [85.2, 90.1, 78.5, 92.3, 88.9]
    
    try:
        diff = weight_difference(sample_weights)
        print(f"Difference between max and min weight is {diff}")
        
        # Test with a larger list to demonstrate efficiency
        large_list = [float(i + 10.5 * (i % 2)) for i in range(10**6)]
        diff_large = weight_difference(large_list)
        print(f"Difference from large list calculation: {diff_large}")
        
    except ValueError as ve:
        print(f"Error encountered: {ve}")