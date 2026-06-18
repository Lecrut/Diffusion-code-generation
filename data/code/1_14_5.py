import numpy as np

def adjust_weights(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified decimal percentage change to every measurement in the input list.
    
    The operation scales each element by (1 + percentage_change). 
    This implementation uses NumPy for vectorized computation, ensuring high performance
    on large datasets while maintaining clarity and precision.

    Parameters:
        weights (list[float]): List of weight measurements as floats or integers.
        percentage_change (float): The change factor as a decimal (e.g., 0.10 for +10%). 
                                   Negative values indicate reduction; e.g., -0.25 reduces by 25%.

    Returns:
        list[float]: A new list containing the adjusted weights, rounded to 4 decimal places.
    
    Raises:
        ValueError: If input is not a list or percentage_change is non-numeric.
    
    Example:
        >>> adjust_weights([10.0, 25], 0.1)
        [11.0, 27.5]
    """

    if not isinstance(weights, list):
        raise ValueError(f"Input 'weights' must be a list; got {type(weights).__name__}")
    
    try:
        percentage_change = float(percentage_change)
    except (TypeError, ValueError):
        raise ValueError("Parameter 'percentage_change' must be numeric.")

    if len(weights) == 0:
        return []

    # Convert input list to numpy array for vectorized operations
    weights_array = np.array([float(w) for w in weights])

    # Vectorized scaling operation using broadcasting (1 + percentage_change is broadcasted across all elements)
    scaled_weights = weights_array * (1.0 + percentage_change)

    return [round(value, 4) if isinstance(value, float) else value 
            for value in scaled_weights]

if __name__ == '__main__':
    # Hard-coded sample values without user input or external dependencies
    original_weights = [5.23, -10.78, 0.0, 42.9999, 1e-6]
    change_factor = 0.15
    
    result_weights = adjust_weights(original_weights, change_factor)

    print("Original Weights:", original_weights)
    print(f"Adjustment: {change_factor * 100:.2f}%")
    print("Adjusted Weights:", result_weights)