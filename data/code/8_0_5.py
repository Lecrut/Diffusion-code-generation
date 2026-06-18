import math

def calculate_rectangle_area(width: float, height: float) -> None:
    """
    Calculate and print the area of a rectangle given its width and height.
    
    Args:
        width (float): The width of the rectangle. Must be non-negative.
        height (float): The height of the rectangle. Must be non-negative.
        
    Raises:
        ValueError: If either dimension is negative or not a number.
    """
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numeric values.")

    if width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative.")

    area = width * height
    print(f"Rectangle Area Calculation:")
    print(f"  Width : {width}")
    print(f"  Height: {height}")
    print(f"  Area  : {area:.2f} square units")

if __name__ == '__main__':
    # Hard-coded sample values for testing, no user input required.
    sample_width = 5.0
    sample_height = 10
    
    try:
        calculate_rectangle_area(sample_width, sample_height)
    except (ValueError, TypeError) as e:
        print(f"An error occurred during calculation: {e}")