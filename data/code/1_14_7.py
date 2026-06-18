import numpy as np

def apply_weight_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change (as a decimal) to every measurement in the input list.
    
    Parameters:
        weights (list of float): Original weight measurements.
        percentage_change (float): The desired percentage change as a decimal (e.g., 0.1 for +10%).
        
    Returns:
        list[float]: New list of adjusted weight measurements.
    """
    # Convert input to numpy array for vectorized operations
    weights_array = np.array(weights, dtype=np.float64)
    
    # Apply the percentage change using vectorized multiplication and broadcasting
    new_weights_array = weights_array * (1 + percentage_change)
    
    # Return as a list of floats
    return [float(val) for val in new_weights_array]

if __name__ == '__main__':
    sample_weights = [50.0, 75.2, 100.0, 33.4, 99.9]
    change_percent = 0.1  # Represents a 10% increase
    
    result = apply_weight_change(sample_weights, change_percent)
    
    print("Original weights:", sample_weights)
    print(f"Percentage change: {change_percent} ({int(change_percent * 100)}%)")
    print("Adjusted weights:", result)