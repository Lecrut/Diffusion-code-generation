import numpy as np

def apply_percentage_change(weights: list[float], change_percent: float) -> list[float]:
    """
    Applies a specified percentage change to every measurement in the input list.
    
    The calculation is performed using NumPy for vectorized operations, ensuring high 
    performance even with large lists of weight measurements.
    
    Parameters:
        weights (list[float]): A list of numerical values representing initial weight measurements.
        change_percent (float): The percentage change as a decimal value. Positive values increase the weight; negative values decrease it. Zero leaves the original values unchanged.
        
    Returns:
        list[float]: A new list containing the modified weight measurements after applying the specified percentage change.

    Example Usage:
        >>> weights = [10, 20, 30]
        >>> apply_percentage_change(weights, 5)
        [10.5, 21.0, 31.5]
        
    Note: This function avoids explicit Python loops over the data by leveraging NumPy's 
    underlying C implementation for efficient vectorized computation.

    Args:
        weights (list[float]): List of weight measurements to be modified.
        change_percent (float): Percentage change as a decimal value.

    Returns:
        list[float]: Modified list with applied percentage changes.
    
    Raises:
        TypeError: If 'weights' is not a list or if elements are non-numeric, and 
                  if 'change_percent' is not numeric.
    """
    # Validate inputs to ensure type safety before conversion
    if not isinstance(weights, (list, tuple)):
        raise TypeError("Input 'weights' must be a list.")

    try:
        weights_array = np.array(weights)
        change_decimal = float(change_percent)
    except ValueError as e:
        raise TypeError(f"Invalid input type for numeric conversion: {e}") from e
    
    # Apply the percentage change vectorized. 
    # Formula: new_weight = original_weight * (1 + percent_change/100)
    factor = 1 + (change_decimal / 100) if isinstance(change_decimal, float) else 1 + change_percent

    modified_array = weights_array * factor
    
    return list(modified_array)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    initial_weights = [75.2, 80.4, 91.3, 68.0]
    percentage_increase_percent: float = 5.0
    
    new_weights_list = apply_percentage_change(initial_weights, percentage_increase_percent)
    
    print("Original weights:", initial_weights)
    print(f"Percentage change applied (decimal): {percentage_increase_percent / 100}")
    print("New weights after applying the change:")
    for i, weight in enumerate(new_weights_list):
        print(f"{i + 1}. {weight:.2f} kg")
    
    # Verify that the function works correctly with a simple check.
    assert new_weights_list[0] == initial_weights[0] * (1 + percentage_increase_percent / 100), "Calculation failed for first element."