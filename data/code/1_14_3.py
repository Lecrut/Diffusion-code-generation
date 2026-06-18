import numpy as np

def apply_percentage_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change to every weight measurement in the input list.
    
    The calculation is performed using NumPy's vectorized operations for efficiency with large lists.
    Formula applied: new_weight = old_weight * (1 + percentage_change_decimal)
    
    Args:
        weights (list[float]): A list of numerical weight measurements.
        percentage_change (float): The decimal representation of the percentage change 
                                  (e.g., 0.1 for a 10% increase, -0.2 for a 20% decrease).
    
    Returns:
        list[float]: A new list containing the modified weights.
    
    Raises:
        ValueError: If input lists are empty or contain non-numeric values.
    """
    if not isinstance(weights, (list, np.ndarray)):
        raise TypeError("Input 'weights' must be a list.")
    
    # Validate that all elements in the weight list are numeric
    for item in weights:
        try:
            float(item)
        except ValueError:
            raise ValueError(f"All items in the weight list must be numeric. Found invalid value: {item}")

    if len(weights) == 0:
        return []

    # Convert input to NumPy array for vectorized computation
    weights_array = np.array(weights, dtype=float)
    
    # Apply the percentage change using broadcasting (vectorized operation)
    modified_weights_array = weights_array * (1 + percentage_change)
    
    # Return as a standard Python list of floats
    return [float(x) for x in modified_weights_array]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    
    initial_weight_measurements = [10.5, 23.7, 45.2, 67.89, 12.3]
    
    percentage_change_decimal = 0.15  # Represents a 15% increase

    result_weights = apply_percentage_change(initial_weight_measurements, percentage_change_decimal)

    print("Original weights:", initial_weight_measurements)
    print(f"Percentage change applied: {percentage_change_decimal * 100}%")
    print("Modified weights:", result_weights)