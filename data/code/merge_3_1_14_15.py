import numpy as np

def apply_percentage_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change (as a decimal multiplier) to every measurement in the input list.
    
    Parameters:
        weights (list of float): The original weight measurements.
        percentage_change (float): The desired change as a scalar (e.g., 0.1 for +10%, -0.2 for -20%).
        
    Returns:
        list[float]: A new list containing the adjusted weight values.
    
    Optimization Note:
        Uses NumPy's vectorized operations to ensure high performance on large lists, avoiding explicit Python loops.
    """
    # Convert input list to numpy array for efficient broadcasting and multiplication
    weights_array = np.array(weights)
    
    # Apply the percentage change directly using vectorized arithmetic
    new_weights = (weights_array + weights_array * percentage_change).tolist()
    
    return new_weights

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    original_weights = [10.5, 23.4, 67.89, 100.0]
    change_percent = 0.1  # Represents a +10% increase

    result_weights = apply_percentage_change(original_weights, change_percent)
    
    print("Original weights:", original_weights)
    print(f"Percentage change ({change_percent} or {int(change_percent * 100)}%)")
    print("Adjusted weights:", result_weights)