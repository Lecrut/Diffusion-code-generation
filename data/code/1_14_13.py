import numpy as np

def apply_weight_change(weights: list[float], change_percent: float) -> list[float]:
    """
    Applies a specified percentage change to every weight measurement in the input list.
    
    The function converts the input list to a NumPy array for vectorized operations,
    performs the multiplication with (1 + change), and returns the result as a new list.
    
    Parameters:
        weights (list[float]): A list of floating-point numbers representing weight measurements.
        change_percent (float): The percentage change as a decimal value 
                               (e.g., 0.1 for 10% increase, -0.2 for 20% decrease).
    
    Returns:
        list[float]: A new list containing the modified weight values.
    
    Examples:
        >>> weights = [50, 60]
        >>> apply_weight_change(weights, 0.1)
        [55.0, 66.0]
    """
    if not isinstance(change_percent, (int, float)):
        raise TypeError("change_percent must be a numeric value.")
    
    weights_array = np.array(weights, dtype=np.float64)
    modified_weights = weights_array * (1 + change_percent)
    return list(modified_weights)

if __name__ == '__main__':
    sample_weights = [50.5, 72.3, 89.1, -5.2]
    growth_rate = 0.15
    
    result = apply_weight_change(sample_weights, growth_rate)
    
    print(f"Original weights: {sample_weights}")
    print(f"Growth rate (decimal): {growth_rate:.4f}")
    print("New weights after applying change:")
    for i, weight in enumerate(result):
        print(f"Weight #{i}: {weight:.2f}")