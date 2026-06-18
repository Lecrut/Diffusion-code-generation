def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    sample_width = 5.0
    sample_height = 3.0

    try:
        area = calculate_rectangle_area(sample_width, sample_height)
        print(f"The area of the rectangle with width {sample_width} and height {sample_height} is {area}.")
    except Exception as e:
        # Although basic arithmetic rarely fails here, this handles potential future edge cases.
        print(f"An error occurred during calculation: {e}")