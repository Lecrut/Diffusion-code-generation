import numpy as np

def apply_weight_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change (as a decimal) to every measurement in the input list.
    
    Parameters:
        weights (list[float]): List of initial weight measurements.
        percentage_change (float): The desired percentage change as a decimal (e.g., 0.1 for 10%).
        
    Returns:
        list[float]: New list of weights after applying the percentage change.
    
    Optimization Note:
        Uses NumPy for vectorized operations to ensure high performance on large datasets,
        avoiding Python-level loops which can be slow with millions of elements.
    """
    # Convert input lists to numpy array for fast broadcasting operation
    arr = np.array(weights)
    # Apply the change using element-wise multiplication: new_value = original * (1 + percentage_change)
    result_arr = arr * (1 + percentage_change)
    return result_arr.tolist()

if __name__ == '__main__':
    sample_weights = [50.0, 75.2, 100.0, 25.3]
    change_factor = 0.10  # Represents a 10% increase
    
    modified_weights = apply_weight_change(sample_weights, change_factor)
    
    print(f"Original weights: {sample_weights}")
    print(f"Applied {change_factor * 100}% change")
    print(f"New weights: {modified_weights}")