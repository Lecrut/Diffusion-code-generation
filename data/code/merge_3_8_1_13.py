def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area as an integer if possible, otherwise rounded to two decimal places.

    Example:
        >>> calculate_area(5, 10)
        50
    """
    result = length * width
    return round(result, 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access
    l_sample = 4.5
    w_sample = 6
    
    calculated_area_result = calculate_area(l_sample, w_sample)
    
    print(f"Calculated area: {calculated_area_result}")