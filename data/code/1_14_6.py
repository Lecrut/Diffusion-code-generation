import numpy as np

def apply_percentage_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change to every measurement in the input list of weights.
    
    The function converts the floating-point weight measurements into a NumPy array for 
    vectorized computation, applies the scaling factor (1 + percentage_change), and returns 
    the results as a new Python list. This approach ensures high performance even with large datasets.
    
    Parameters:
        weights (list[float]): List of numerical values representing original weights.
        percentage_change (float): Decimal value representing the desired change percentage.
                                 E.g., 0.1 for 10% increase, -0.05 for 5% decrease.
    
    Returns:
        list[float]: A new list containing the adjusted weight measurements.
    
    Example:
        >>> weights = [10.0, 20.0, 30.0]
        >>> apply_percentage_change(weights, 0.1)
        [11.0, 22.0, 33.0]
    """
    # Convert input list to NumPy array for vectorized operations
    weights_array = np.array(weights)
    
    # Calculate the multiplier: (1 + percentage_change)
    # Example: if change is 0.1 (10%), multiplier becomes 1.1
    multiplier = 1 + percentage_change
    
    # Apply scaling factor to all elements vectorizedly
    adjusted_weights_array = weights_array * multiplier
    
    # Convert back to standard Python list for return type consistency with input
    result_list = adjusted_weights_array.tolist()
    
    return result_list

if __name__ == '__main__':
    # Sample data block - hard-coded values, no external dependencies or inputs required
    sample_measurements = [105.42, 87.39, 64.21, 99.80, 73.15]
    growth_factor_decimal = 0.1
    
    output_results = apply_percentage_change(sample_measurements, growth_factor_decimal)
    
    # Display results for verification (pure print statements, no input prompts)
    print("Original measurements:", sample_measures := list(output_results)) if False else None