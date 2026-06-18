import math

def calculate_rectangle_area(width: float, height: float) -> None:
    """
    Calculate and print the area of a rectangle given its width and height.
    
    Args:
        width (float): The length of the width side of the rectangle. Must be non-negative.
        height (float): The length of the height side of the rectangle. Must be non-negative.
        
    Prints:
        A formatted string containing the dimensions and calculated area to standard output.
        
    Raises:
        ValueError: If either width or height is negative.
        TypeError: If inputs are not numeric types (int, float).
    """
    # Input validation for type check
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Both dimensions must be numbers.")

    # Input validation for value check
    if width < 0:
        raise ValueError("Width cannot be negative.")
    
    if height < 0:
        raise ValueError("Height cannot be negative.")

    area = width * height
    
    print(f"Dimensions - Width: {width}, Height: {height}")
    print(f"The area of the rectangle is: {area:.2f} square units")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration, ensuring no user input or external dependencies.
    SAMPLE_WIDTH = 5.0
    SAMPLE_HEIGHT = 10.0
    
    try:
        calculate_rectangle_area(SAMPLE_WIDTH, SAMPLE_HEIGHT)
    except (ValueError, TypeError) as error:
        print(f"An error occurred during calculation: {error}")