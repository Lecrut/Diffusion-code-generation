def calculate_dimension_ratio(length: float, width: float) -> dict:
    """
    Calculates the ratio between two dimensions.

    Args:
        length (float): The first dimension value; must be positive.
        width (float): The second dimension value; must be positive.

    Returns:
        dict: A dictionary containing 'length', 'width' as floats, 
              and 'ratio' calculated to 4 decimal places. If input validation fails, returns None or raises an error based on implementation choice.
    
    Raises:
        ValueError: If either length or width is not positive.

    Example:
        >>> calculate_dimension_ratio(10, 5)
        {'length': 10.0, 'width': 5.0, 'ratio': 2.0}
    """
    # Input constraint validation: both lengths must be strictly greater than zero
    if length <= 0 or width <= 0:
        raise ValueError("Both dimensions must be positive numbers.")

    result_ratio = round(length / width, 4)

    return {
        'length': float(length),
        'width': float(width),
        'ratio': result_ratio
    }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_length = 12.5
    sample_width = 4

    print(f"Input: Length={sample_length}, Width={sample_width}")
    
    try:
        ratio_data = calculate_dimension_ratio(sample_length, sample_width)
        
        # Display results if valid inputs provided positive values
        result_text = f"{ratio_data['length']} : {ratio_data['width']} -> Ratio is {ratio_data['ratio']}"
        print(result_text)

    except ValueError as ve:
        print(f"Error occurred during calculation due to input constraints: {ve}")