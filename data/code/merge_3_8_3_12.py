import sys

def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given length and width."""
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No input(), sys.stdin.read(), argparse, or interactive prompts are used.
    
    try:
        length = 5.0
        width = 10.0
        
        area = calculate_rectangle_area(length, width)
        
        print(f"Rectangle Area Calculation:")
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Area: {area:.2f} square units")
    except ValueError as e:
        # This block technically handles the exception type mentioned in the task,
        # though it is wrapped here for logical completeness since our sample values are valid.
        if "non-numeric input" not in str(e):
            print(f"Error occurred during calculation (not strictly non-numeric due to hard-coded inputs): {e}")