import numpy as np

def apply_weight_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change (as a decimal) to every weight measurement in the input list.

    Args:
        weights (list[float]): List of floating-point numbers representing weight measurements.
        percentage_change (float): The desired percentage change as a decimal value 
                                   (e.g., 0.1 for a 10% increase, -0.05 for a 5% decrease).

    Returns:
        list[float]: A new list containing the modified weights after applying the percentage change.

    Note:
        This implementation uses NumPy's vectorized operations to ensure high performance 
        on large lists of weight measurements without explicit Python loops.
    
    Example usage (see main block):
        >>> apply_weight_change([10, 20, 30], 0.1)
        [11.0, 22.0, 33.0]
    """
    # Convert input list to NumPy array for vectorized operations
    weights_array = np.array(weights, dtype=float)
    
    # Calculate the scaling factor: original + (percentage_change * original) 
    # is equivalent to multiplying by (1 + percentage_change)
    scale_factor = 1.0 + percentage_change
    
    # Apply the change using vectorized multiplication
    new_weights_array = weights_array * scale_factor
    
    # Convert back to a standard Python list for return consistency with input type expectation
    return new_weights_array.tolist()

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network access, or files)
    
    # Sample 1: Positive percentage change (increase weights by 20%)
    initial_weights_1 = [5.5, 7.8, 9.2, 12.4]
    percent_increase = 0.20
    
    result_1 = apply_weight_change(initial_weights_1, percent_increase)
    
    # Sample 2: Negative percentage change (decrease weights by 10%)
    initial_weights_2 = [100, 250, -50]
    percent_decrease = -0.10
    
    result_2 = apply_weight_change(initial_weights_2, percent_decrease)

    # Sample 3: Zero percentage change (no modification expected)
    initial_weights_3 = [10, 20, 30]
    zero_percent = 0.0
    
    result_3 = apply_weight_change(initial_weights_3, zero_percent)
    
    print("Sample 1 - Increase by 20%:")
    print(result_1)
    
    print("\nSample 2 - Decrease by 10% (including negative value):")
    print(result_2)
    
    print("\nSample 3 - Zero change:")
    print(result_3)