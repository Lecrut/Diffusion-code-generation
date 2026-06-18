def weight_range(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    This function is optimized to handle large lists by avoiding multiple passes 
    over the data if possible, though standard min/max operations are O(n).
    For extremely large datasets where memory allocation of two separate sets 
    (one for max tracking, one for min) might be an issue, a single pass could 
    theoretically be used, but Python's built-in C-optimized min and max functions 
    are typically faster than manual loops in pure Python.

    Parameters:
        weights (list): A list of numerical values representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum weight.
                      Raises ValueError if the input is empty.
                      
    Exceptions:
        TypeError: If 'weights' is not a list.
        ValueError: If 'weights' is an empty list.
    """
    if not isinstance(weights, list):
        raise TypeError("Input must be a list.")
    
    if len(weights) == 0:
        raise ValueError("Cannot calculate range of an empty list.")

    return max(weights) - min(weights)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    small_list = [10, 20, 30]
    large_simulated_data = list(range(1_000_000)) + [-50, -49, -48]

    print(f"Small list range: {weight_range(small_list)}")
    
    # Using a generator expression to simulate potentially very large data efficiently.
    huge_generator = (i for i in range(10_000_000)) + [float('inf'), float('-inf')]
    
    try:
        # Note: max() and min() on generators are efficient but consume the generator once each.
        # To truly optimize a single pass, one would need to implement it in C or use numpy.
        # However, for standard Python lists/generators, this is the most direct approach.
        huge_list = list(huge_generator) 
        print(f"Huge data range: {weight_range(huge_list)}")
    except Exception as e:
        print(f"Error processing large dataset: {e}")