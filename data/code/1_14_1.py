import numpy as np

def apply_percentage_change(weights: list[float], percentage_change: float) -> list[float]:
    """
    Applies a specified percentage change (as a decimal) to every measurement in the input list.
    
    Parameters:
        weights (list of float): List of weight measurements.
        percentage_change (float): The percentage change as a decimal (e.g., 0.1 for 10%).
        
    Returns:
        list[float]: New list with adjusted weights.
    """
    # Convert input to numpy array for vectorized operations
    arr = np.array(weights, dtype=np.float64)
    
    # Apply the percentage change using broadcasting and multiplication
    new_arr = arr * (1 + percentage_change)
    
    # Return as a list of floats
    return [float(x) for x in new_arr]

if __name__ == '__main__':
    sample_weights = [50.0, 75.2, 30.8, 90.1, 45.6]
    percentage_change_decimal = 0.1

    result = apply_percentage_change(sample_weights, percentage_change_decimal)
    
    print("Original weights:", sample_weights)
    print(f"Percentage change: {percentage_change_decimal}")
    print("Adjusted weights:", result)