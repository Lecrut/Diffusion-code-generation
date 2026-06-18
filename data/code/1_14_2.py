import numpy as np

def apply_percentage_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change to every weight measurement in the input list.
    
    The calculation is performed using vectorized NumPy operations for efficiency with large lists.
    Formula: new_weight = old_weight * (1 + percentage_change_decimal)
    
    Args:
        weights (list[float]): List of initial weight measurements.
        percentage_change (float): Decimal representation of the percentage change 
                                  (e.g., 0.10 for a 10% increase, -0.05 for a 5% decrease).
    
    Returns:
        list[float]: A new list containing the modified weights.
    """
    # Convert input to NumPy array for vectorized operations
    weight_array = np.array(weights)
    
    # Calculate scaling factor and apply change using broadcasting (vectorized operation)
    scaled_weights = weight_array * (1 + percentage_change)
    
    # Return as a standard Python list of floats
    return [float(x) for x in scaled_weights]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    initial_weights = [50.0, 120.5, 34.9, 87.6, 200.0]
    change_rate = 0.15  # Represents a 15% increase

    result_weights = apply_percentage_change(initial_weights, change_rate)

    print("Original weights:", initial_weights)
    print(f"Percentage change: {change_rate * 100}%")
    print("New weights:", result_weights)