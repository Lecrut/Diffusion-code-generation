def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sample_width = 5.0
    sample_height = 3.0

    try:
        calculated_area = calculate_rectangle_area(sample_width, sample_height)
        print(f"The area of a rectangle with width {sample_width} and height {sample_height} is {calculated_area}")
    except Exception as e:
        # Graceful error handling for unexpected issues during calculation
        print(f"An error occurred while calculating the area: {e}")