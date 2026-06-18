def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given its length and width."""
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    try:
        length = 5.0
        width = 10.0
        
        area = calculate_rectangle_area(length, width)
        
        print(f"Rectangle dimensions: {length} x {width}")
        print(f"Calculated Area: {area}")
    
    except ValueError as e:
        # This block is technically unreachable with the hard-coded values above, 
        # but included to demonstrate error handling capability if inputs were dynamic.
        print("Error:", str(e))