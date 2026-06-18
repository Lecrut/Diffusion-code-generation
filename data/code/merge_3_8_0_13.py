def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    return round(abs(width) * abs(height), 2)

if __name__ == '__main__':
    # Hard-coded sample values to ensure script runs without user input or arguments
    sample_width = 5.0
    sample_height = 3.5
    
    area = calculate_rectangle_area(sample_width, sample_height)
    
    print(f"Rectangle dimensions: {sample_width} x {sample_height}")
    print(f"Calculated Area: {area}")