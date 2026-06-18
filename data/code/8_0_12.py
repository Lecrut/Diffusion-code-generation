import math

def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")
    
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    sample_width = 5.0
    sample_height = 10.5
    
    try:
        area = calculate_rectangle_area(sample_width, sample_height)
        print(f"The area of the rectangle is {area}.")
    except ValueError as e:
        print(f"Error calculating area: {e}")