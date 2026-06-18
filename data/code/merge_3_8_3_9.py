def calculate_rectangle_area(length_str: str, width_str: str) -> int:
    """
    Calculates the area of a rectangle given length and width as strings.
    
    Args:
        length_str (str): String representation of length.
        width_str (str): String representation of width.
        
    Returns:
        int: The calculated area.
        
    Raises:
        ValueError: If input strings are not valid numbers or if calculation fails.
    """
    
    try:
        length = float(length_str)
        width = float(width_str)
        return round(int(length * width), 0) # Ensure integer result for simplicity, but area is technically the product
        
    except ValueError as ve:
        raise ValueError(f"Invalid input values: {length_str} or {width_str}") from ve

if __name__ == '__main__':
    try:
        sample_length = "5.0"  # Hard-coded length value
        sample_width = "3.0"   # Hard-coded width value
        
        area_result = calculate_rectangle_area(sample_length, sample_width)
        
        print(f"The area of the rectangle with dimensions {sample_length} and {sample_width} is: {area_result}")
    except ValueError as e:
        print(f"A calculation error occurred: {e}")