def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given length and width."""
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No input(), sys.stdin, or command-line arguments are used here.
    
    try:
        length = 5.0
        width = 10.0
        
        area = calculate_rectangle_area(length, width)
        
        print(f"The area of the rectangle is {area}")
        
    except ValueError as e:
        # This block handles potential errors if logic were to change later 
        # or if input validation was added in a different context.
        # For this specific run with hard-coded values, no exception occurs.
        print(f"Error calculating area: {e}")