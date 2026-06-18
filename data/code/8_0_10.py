def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    sample_width = 5.0
    sample_height = 3.0

    area = calculate_rectangle_area(sample_width, sample_height)

    print(f"Rectangle Area Calculation")
    print("=" * 25)
    print(f"Width: {sample_width}")
    print(f"Height: {sample_height}")
    print("-" * 25)
    print(f"Area: {area} square units")