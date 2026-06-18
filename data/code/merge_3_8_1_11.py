from typing import Union

def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area as the product of length and width.

    Raises:
        TypeError: If either length or width is not a numeric type.
        ValueError: If either length or width is negative.
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both length and width must be numbers.")

    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")

    return length * width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    sample_length = 5.0
    sample_width = 3.0
    
    area_result = calculate_area(sample_length, sample_width)
    
    print(f"Area of rectangle with length {sample_length} and width {sample_width}:")
    print(f"{area_result}")