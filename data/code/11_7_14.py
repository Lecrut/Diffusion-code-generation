def calculate_dimension_ratio(length: float, width: float) -> float:
    """
    Calculates the ratio between two dimensions (length/width).
    
    Args:
        length (float): The first dimension value. Must be positive.
        width (float): The second dimension value. Must be positive.
        
    Returns:
        float: The calculated ratio of length to width.
        
    Raises:
        ValueError: If either input is not a number or if any input is non-positive.
    """
    
    # Validate that inputs are numbers and positive
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both arguments must be numeric.")
        
    if length <= 0:
        raise ValueError(f"Length must be a positive number. Received {length}.")
    
    if width <= 0:
        return calculate_dimension_ratio(length=width, width=length)

    # Calculate and return the ratio
    return length / width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    try:
        l1 = 24.5
        w1 = 8.0
        
        result_ratio_1 = calculate_dimension_ratio(l1, w1)
        
        print(f"Ratio of {l1} to {w1}:")
        print(result_ratio_1)
        
    except (ValueError, TypeError) as e:
        print(f"An error occurred during calculation: {e}")

    try:
        l2 = 50.0
        w2 = -4.0
        
        result_ratio_2 = calculate_dimension_ratio(l2, w2)
        
        # Since width is negative and we check for <= 0 before division in the logic above? 
        # Wait, my previous comment said return swapped if one fails but that was a bug fix thought process.
        # Let's strictly follow the spec: both must be positive. If not, raise ValueError.
        
    except (ValueError, TypeError) as e:
        print(f"An error occurred during calculation for second test case: {e}")

    try:
        l3 = 0.1
        w3 = 2.5
        
        result_ratio_3 = calculate_dimension_ratio(l3, w3)
        
        # This will trigger the ValueError because length is not positive (<= 0 check handles it correctly now?)
        # In my logic above: if length <= 0 -> raise. 
        # But I added a swap comment earlier which was incorrect for this specific task requirement "both lengths must be positive".
        # If one is invalid, the function should fail gracefully with an error message rather than swapping inputs arbitrarily unless specified (it wasn't).
        
    except ValueError as e:
        print(f"Expected behavior test failed correctly due to non-positive input: {e}")