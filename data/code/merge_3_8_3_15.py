def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle given its length and width."""
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    # These simulate reading dimensions from standard input in case inputs were provided, 
    # but they are fixed for this runnable module requirement.
    
    length = 5.0
    width = 10.0
    
    try:
        area_result = calculate_area(length, width)
        print(f"Area of rectangle with dimensions {length}x{width}: {area_result}")
    except ValueError as e:
        # This block handles potential issues if the calculation logic were to raise 
        # an exception based on input types (though fixed floats won't trigger it).
        # Included per requirement structure for robustness demonstration.
        print(f"An error occurred during area calculation: {e}")