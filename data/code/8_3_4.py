import sys

def calculate_rectangle_area(length: float | None = None, width: float | None = None) -> int | str:
    """
    Calculates the area of a rectangle given length and width.
    
    Args:
        length (float): The length of the rectangle. Defaults to 10 if not provided.
        width (float): The width of the rectangle. Defaults to 5 if not provided.
        
    Returns:
        int or str: The calculated area as an integer, or a string indicating failure reasons.
    
    Raises:
        ValueError: If length or width is None and defaults are expected but missing in specific contexts (though this function uses defaults).
                   Note: This implementation assumes valid numeric input based on the prompt's requirement to handle non-numeric exceptions via try-except blocks around calculation logic if inputs were dynamic. Since we use hardcoded values, no ValueError will occur here unless modified for testing purposes later.
    """
    # Ensure length and width are not None (though defaults prevent this in main block)
    if length is None:
        length = 10
    
    if width is None:
        width = 5

    try:
        area = int(length * width)
        return area
    except TypeError as e:
        # This handles cases where inputs might not be numeric in broader usage, 
        # though strictly with floats it won't raise here unless converted incorrectly.
        raise ValueError(f"Invalid input for calculation: {e}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or interactive prompts)
    length = 10
    width = 5

    try:
        area_result = calculate_rectangle_area(length, width)
        print(f"Area of rectangle with dimensions {length}x{width}: {area_result}")
    except ValueError as ve:
        # This block demonstrates handling of potential exceptions if inputs were invalid 
        # (though hardcoded values here are safe). In a dynamic scenario, this would catch non-numeric input.
        print(f"Error calculating area: {ve}", file=sys.stderr)