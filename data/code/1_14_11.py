import numpy as np

def apply_weight_change(measurements: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change (as a decimal, e.g., 0.1 for +10%) 
    to every measurement in the input list and returns the new list of weights.

    Parameters:
        measurements (list of float): The original weight measurements.
        percentage_change (float): The desired change as a decimal value.

    Returns:
        list[float]: A new list containing the adjusted weight measurements.
    
    Optimization Note:
        Uses NumPy for vectorized operations to ensure high performance on large lists,
        avoiding explicit Python loops which are significantly slower in such cases.
    """
    # Convert input list to a numpy array for efficient vectorized computation
    arr = np.array(measurements)

    # Calculate the multiplier based on the percentage change (1 + decimal_change) and apply it element-wise
    adjusted_arr = arr * (1 + percentage_change)

    # Return as a standard Python list of floats to match the expected return type exactly
    return [float(x) for x in adjusted_arr]

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    original_weights = [10.5, 23.7, 45.9, 67.8, 12.3, 89.1]

    # Sample percentage change: increase by 15% (represented as decimal 0.15)
    growth_rate = 0.15

    new_weights = apply_weight_change(original_weights, growth_rate)

    print("Original weights:", original_weights)
    print(f"Applying {growth_rate * 100}% change...")
    print("Adjusted weights:", new_weights)