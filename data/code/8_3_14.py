def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given length and width."""
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values to avoid any user input or interactive prompts.
    try:
        length = 5.0
        width = 10.0
        
        area = calculate_rectangle_area(length, width)
        
        print(f"Rectangle dimensions: {length} x {width}")
        print(f"Calculated Area: {area}")
        
    except ValueError as e:
        # This block is technically unreachable with hard-coded values but 
        # demonstrates the required error handling structure.
        print("Error:", str(e))