import numpy as np

def apply_weight_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change to every measurement in the input weight list.
    
    The function converts the integer or floating-point input weights into an array, 
    applies the scaling factor (1 + percentage_change), and returns the resulting values as a new list.
    
    This implementation uses NumPy for vectorized operations to ensure high performance on large lists.
    
    Parameters:
        weights (list[float]): A list of weight measurements.
        percentage_change (float): The desired change in decimal form. 
                                  Positive value increases the weights, negative decreases them.
    
    Returns:
        list[float]: A new list containing the adjusted weight values.
    
    Example usage:
        >>> original_weights = [10.5, 20.3, 30.7]
        >>> result = apply_weight_change(original_weights, 0.1) 
        # Result will be approximately [11.55, 22.33, 33.77]
    """
    
    if not weights:
        return []

    # Convert input list to numpy array for vectorized computation
    weight_array = np.array(weights, dtype=np.float64)
    
    # Compute the scaling factor and apply it element-wise (vectorized operation)
    adjusted_weights = weight_array * (1 + percentage_change)
    
    # Return as a standard Python list of floats
    return [float(val) for val in adjusted_weights]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    original_samples = [50.2, 100.0, -10.5, 75.33, 0.0]
    change_rate = 0.2

    result_list = apply_weight_change(original_samples, change_rate)

    print("Original weights:", original_samples)
    print(f"Percentage change: {change_rate * 100:.1f}%")
    print("Adjusted weights:", result_list)