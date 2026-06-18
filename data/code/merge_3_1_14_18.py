import numpy as np

def apply_percentage_change(weights: list[float], percent_change: float) -> list[float]:
    """
    Applies a specified percentage change to every weight in the input list.
    
    The new value is calculated as: original_value * (1 + decimal_percent).
    
    Parameters
    ----------
    weights : list of float
        List of initial weight measurements.
    percent_change : float
        Percentage change as a decimal (e.g., 0.1 for 10% increase, -0.2 for 20% decrease).

    Returns
    -------
    list[float]
        New list containing the adjusted weights.
    
    Notes
       Uses NumPy vectorization for high performance on large lists without explicit Python loops.
    """
    # Convert input to numpy array for efficient vectorized operations
    weight_array = np.array(weights, dtype=float)
    
    # Apply percentage change: new_value = old_value * (1 + percent_change)
    adjusted_weights = weight_array * (1 + percent_change)
    
    return adjusted_weights.tolist()

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies beyond standard libs and NumPy.
    initial_weights = [50, 75, 62.5, 100]
    change_percent = 0.20  # Represents a 20% increase

    result_weights = apply_percentage_change(initial_weights, change_percent)
    
    print(f"Original weights: {initial_weights}")
    print(f"Percentage change applied: {change_percent * 100}%")
    print(f"Adjusted weights: {result_weights}")