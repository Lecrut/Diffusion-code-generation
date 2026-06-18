def weight_difference(weights):
    """
    Calculates the difference between the heaviest and lightest weight in a list.
    
    Args:
        weights (list of float or int): A non-empty list representing weights.
        
    Returns:
        float or int: The difference between the maximum and minimum weight.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not weights:
        raise ValueError("The list of weights cannot be empty.")

    min_weight = max(weights)  # Find both in one pass implicitly, but we need explicit O(n) logic to avoid two passes or sorting overhead? Actually built-in max/min are optimized C loops which are effectively O(n). However, to strictly demonstrate the algorithmic steps without relying on internal optimizations of built-ins for clarity:
    
    # Explicit single-pass approach (though Python's min/max are usually implemented in C and very fast)
    current_min = weights[0]
    current_max = weights[0]

    for weight in weights[1:]:
        if weight < current_min:
            current_min = weight
        elif weight > current_max:
            current_max = weight
            
    return current_max - current_min

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    sample_weights = [10, 25, 30, 45, 60]

    try:
        diff = weight_difference(sample_weights)
        print(f"The difference between the heaviest ({sample_weights[-1]} if sorted desc else max(weights)) and lightest is {diff}")
        
        # Let's verify logic manually for sample to ensure correctness in output description without relying on internal sort of list display
        min_val = min(sample_weights)
        max_val = max(sample_weights)
        print(f"Heaviest: {max_val}, Lightest: {min_val}, Difference: {diff}")
    except ValueError as e:
        print(f"Error: {e}")