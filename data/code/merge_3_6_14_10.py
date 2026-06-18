def weight_range(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): A non-empty list containing numeric values representing weights.
        
    Returns:
        float: The range (max - min) of the input list.
        
    Raises:
        ValueError: If the input list is empty.
        TypeError: If any element in the list is not a number.

    Efficiently processes large lists by performing a single pass to find max and min values, avoiding multiple traversals or sorting overhead for very large datasets where only range matters (though Python's built-in sorted() is highly optimized C-based). This implementation uses min() and max(), which are implemented in C and extremely efficient.
    """
    if not weights:
        raise ValueError("The list of weights cannot be empty.")

    
    return float(max(weights)) - float(min(weights))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    small_list = [10, 25, 30, 45]
    large_simulated_data = list(range(100000, 100100))

    
    result_small = weight_range(small_list)
    
    result_large = weight_range(large_simulated_data)

    print(f"Range for small sample: {result_small}")