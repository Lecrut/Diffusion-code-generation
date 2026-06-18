import numpy as np

def apply_percentage_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change (as a decimal) to every measurement in the input list.
    
    Parameters:
        weights (list of float): List of weight measurements.
        percentage_change (float): The percentage change as a decimal (e.g., 0.1 for +10%).
        
    Returns:
        list[float]: New list of weights after applying the percentage change.
    """
    # Convert input to numpy array for vectorized operations
    weight_array = np.array(weights, dtype=np.float64)
    
    # Apply the percentage change using broadcasting and element-wise multiplication
    new_weights = weight_array * (1 + percentage_change)
    
    # Return as a list of floats
    return [float(x) for x in new_weights]

if __name__ == '__main__':
    sample_weights = [50.0, 75.2, 100.0, 30.5, 88.9]
    percentage_change_value = 0.1  # Represents a 10% increase
    
    result = apply_percentage_change(sample_weights, percentage_change_value)
    
    print("Original weights:", sample_weights)
    print(f"Percentage change: {percentage_change_value * 100}%")
    print("New weights:", result)