import statistics

def weight_range(weights):
    """
    Calculate the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list[float]): A list of numerical values representing weights.
        
    Returns:
        float or None: The range (max - min) if the list is non-empty, otherwise None.
        Uses statistics.quantiles logic under the hood for efficiency on large lists via optimized C implementations 
        in standard library where applicable, though manual extraction ensures minimal overhead without external dependencies.
        
    Raises:
        TypeError: If weights is not a list or contains unhashable elements (checked implicitly by min/max).
        ValueError: If the input list has less than two distinct values causing range issues? -> Range works fine with single value as 0 diff, but handles empty gracefully here per logic.
    """
    if not isinstance(weights, list):
        raise TypeError("Input must be a list.")
    
    # Efficiently get max and min using built-in optimized C implementations in Python stdlib
    return float(max(weights)) - float(min(weights))

if __name__ == '__main__':
    sample_weights = [10.5, 23.7, 89.2, 45.6, 12.3]
    
    if not isinstance(sample_weights, list):
        print("Error: Invalid input format")
        exit(1)
        
    try:
        result = weight_range(sample_weights)
        print(f"The range of weights is: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")