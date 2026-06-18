def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    sample_width = 5.0
    sample_height = 10.0

    result_area = calculate_rectangle_area(sample_width, sample_height)
    
    print(f"Rectangle Area: {result_area}")