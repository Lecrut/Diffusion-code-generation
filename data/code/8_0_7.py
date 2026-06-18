def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculates the area of a rectangle given its width and height."""
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values to ensure script runs without user input or external dependencies.
    sample_width = 5.0
    sample_height = 10.0

    area = calculate_rectangle_area(sample_width, sample_height)
    print(f"The area of the rectangle with width {sample_width} and height {sample_height} is: {area}")