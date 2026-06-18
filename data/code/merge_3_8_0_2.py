def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No user input, command-line arguments, network access, or file I/O is used.
    sample_width = 5.0
    sample_height = 3.5
    
    try:
        area = calculate_rectangle_area(sample_width, sample_height)
        print(f"The area of the rectangle with width {sample_width} and height {sample_height} is:")
        print(area)
    except ValueError as ve:
        print(str(ve))