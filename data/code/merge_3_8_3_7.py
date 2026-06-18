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
        print(f"Area: {area}")
    
    except ValueError as e:
        # This block is structured to handle potential errors if the logic were extended 
        # to parse input dynamically. Since inputs are hard-coded here, this exception 
        # will not be triggered in normal execution but demonstrates proper error handling structure.
        print(f"Error calculating area: {e}")