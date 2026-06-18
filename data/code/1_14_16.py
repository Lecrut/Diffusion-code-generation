import numpy as np

def apply_percentage_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change to every measurement in the input list.
    
    The calculation is performed using NumPy vectorization for performance on large lists,
    avoiding explicit Python loops which would be slower due to interpreter overhead.
    
    Parameters:
        weights (list of float): List of weight measurements.
        percentage_change (float): Percentage change as a decimal (e.g., 0.10 for +10%).
        
    Returns:
        list[float]: New list of weights after applying the percentage change.
    """
    if not isinstance(weights, (list, tuple)):
        raise TypeError("Input 'weights' must be a list or tuple.")
    
    # Convert to numpy array for vectorized operations
    arr = np.array(weights)
    
    # Apply the percentage change: new_value = old_value * (1 + change)
    result_array = arr * (1.0 + percentage_change)
    
    # Return as a list of floats
    return [float(x) for x in result_array]

if __name__ == '__main__':
    sample_weights = [50.0, 75.5, 120.3, 89.9, 45.6]
    change_rate = 0.15

    new_weights = apply_percentage_change(sample_weights, change_rate)
    
    print("Original weights:", sample_weights)
    print(f"Percentage change: {change_rate}")
    print("New weights after applying percentage change:")
    for i, weight in enumerate(new_weights):
        print(f"{i + 1}. {weight:.2f} kg")