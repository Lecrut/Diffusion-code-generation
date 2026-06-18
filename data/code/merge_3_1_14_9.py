import numpy as np

def apply_percentage_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change to every weight measurement in the input list.
    
    The calculation is performed using vectorized NumPy operations for efficiency with large lists.
    A positive percentage_change increases weights, while a negative value decreases them.
    
    Args:
        weights (list[float]): List of initial weight measurements.
        percentage_change (float): Decimal representation of the percentage change 
                                  (e.g., 0.10 for 10% increase).
    
    Returns:
        list[float]: New list containing adjusted weight measurements.
    """
    # Convert input to NumPy array for vectorized operations
    weights_array = np.array(weights, dtype=np.float64)
    
    # Apply the percentage change using broadcasting and multiplication
    new_weights_array = weights_array * (1 + percentage_change)
    
    # Return as a list of floats
    return [float(val) for val in new_weights_array]

if __name__ == '__main__':
    sample_weights = [50.0, 75.2, 30.8, 90.1, 45.5]
    change_percent = 0.15

    result = apply_percentage_change(sample_weights, change_percent)
    
    print(f"Original weights: {sample_weights}")
    print(f"Percentage change applied: {change_percent * 100}%")
    print(f"Adjusted weights: {result}")