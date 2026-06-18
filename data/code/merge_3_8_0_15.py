def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_width = 5.0
    sample_height = 3.0

    calculated_area = calculate_rectangle_area(sample_width, sample_height)
    
    print(f"Rectangle Area Calculation")
    print(f"Width: {sample_width}")
    print(f"Height: {sample_height}")
    print(f"Calculated Area: {calculated_area:.2f} square units")