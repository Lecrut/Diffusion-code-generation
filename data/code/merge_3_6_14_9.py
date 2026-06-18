import statistics

def calculate_weight_difference(weights):
    """
    Calculates the difference between the maximum and minimum weight in a list.
    
    Args:
        weights (list of float or int): List of numerical values representing weights.
        
    Returns:
        float: The difference between max and min weight, rounded to 5 decimal places 
               for efficiency with floating-point comparisons on large datasets.
        
    Raises:
        ValueError: If the input list is empty or contains non-numeric values.
    """
    if not weights:
        raise ValueError("Input list must contain at least one value.")

    try:
        min_val = float(min(weights))
        max_val = float(max(weights))
    except TypeError as e:
        raise ValueError(f"All elements in the weight list must be numeric. Error encountered: {e}") from e
    
    return round((max_val - min_val), 5)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    small_weights = [10, 20, 30]
    
    large_sample_data = list(range(1_000_000)) + [5000.0] * 9
    
    print(f"Difference in small sample: {calculate_weight_difference(small_weights)}")
    print(f"Difference in large sample (approx): {calculate_weight_difference(large_sample_data[:10])}") # Testing with subset for clarity if memory is constrained, otherwise full list works efficiently as O(n)