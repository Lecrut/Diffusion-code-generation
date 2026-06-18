def calculate_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area as length multiplied by width.

    Raises:
        TypeError: If either argument is not a number.
        ValueError: If either argument is negative.
    
    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both length and width must be numeric.")
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")

    return length * width

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_values = [10, 5]
    
    area_result = calculate_area(sample_values[0], sample_values[1])
    print(f"Area for dimensions {sample_values[0]}x{sample_values[1]} is: {area_result}")

    # Additional test case with decimal inputs
    dec_sample_values = [7.5, 4]
    
    area_decimal = calculate_area(dec_sample_values[0], dec_sample_values[1])
    print(f"Area for dimensions {dec_sample_values[0]}x{dec_sample_values[1]} is: {area_decimal}")

    # Test error handling example (uncomment to see in action)
    # try:
    #     calculate_area(-2, 5)
    # except ValueError as e:
    #     print(f"Error caught: {e}")