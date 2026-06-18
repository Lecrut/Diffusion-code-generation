import numpy as np

def apply_percentage_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change to every measurement in the input list.
    
    The calculation is performed using vectorized NumPy operations for efficiency 
    with large lists, then converted back to a standard Python list of floats.

    Parameters:
        weights (list[float]): A list of weight measurements.
        percentage_change (float): The desired change as a decimal (e.g., 0.1 for +10%).

    Returns:
        list[float]: A new list containing the adjusted weight measurements.
    
    Example:
        >>> apply_percentage_change([10, 20], 0.5)
        [15.0, 30.0]
    """
    # Convert input to numpy array for vectorized operations
    weights_array = np.array(weights, dtype=float)
    
    # Apply the percentage change: new_value = original * (1 + percentage_change)
    adjusted_weights = weights_array * (1 + percentage_change)
    
    # Return as a standard Python list of floats
    return [float(x) for x in adjusted_weights]

if __name__ == '__main__':
    sample_weights = [50.0, 75.2, 100.0, 33.4]
    change_percent = 0.2
    
    result = apply_percentage_change(sample_weights, change_percent)
    
    print(f"Original weights: {sample_weights}")
    print(f"Percentage change applied: {change_percent * 100}%")
    print(f"Adjusted weights: {result}")