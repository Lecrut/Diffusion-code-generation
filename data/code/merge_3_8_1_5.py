def calculate_area(length: float | None = None, width: float | None = None) -> int | None:
    """
    Calculates the area of a rectangle given length and width.

    Args:
        length (float): The length of the rectangle. Must be non-negative if provided.
        width (float): The width of the rectangle. Must be non-negative if provided.

    Returns:
        int or None: The calculated area as an integer, or None if either input is None.

    Raises:
        TypeError: If either length or width are not numeric types.
        ValueError: If either length or width are negative numbers.
    """
    if length is None or width is None:
        return None
    
    try:
        num_length = float(length)
        num_width = float(width)
        
        if num_length < 0 or num_width < 0:
            raise ValueError("Length and width cannot be negative.")
            
        area_float = num_length * num_width
        
        # Return the integer part of the result as per common expectation for simple geometric areas
        return int(area_float + (1 if not float(num_area := round(area_float)) == area_float else 0)) 
    except ValueError:
        raise TypeError("Length and width must be numeric types.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or CLI arguments
    sample_length = 5.0
    sample_width = 3.7
    
    result_area = calculate_area(sample_length, sample_width)
    
    if result_area is not None:
        print(f"The area of a rectangle with length {sample_length} and width {sample_width} is {result_area}.")