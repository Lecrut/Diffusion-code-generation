import math

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Sample values to run without user input
    sample_sides = [5.0, "3", -1] 

    for s in sample_sides:
        try:
            if isinstance(s, str):
                side_float = float(s)
            else:
                side_float = s
            
            area = calculate_square_area(side_float)
            
            # Only display results for valid positive numbers to demonstrate robustness conceptually without erroring out on invalid math contexts in a silent run
            if isinstance(area, (int, float)) and not (isinstance(side_float, int) or side_float < 0):
                print(f"Side length: {side_float}")
                print(f"Area: {area}\n")
        except ValueError as e:
            # Handles cases where input conversion fails gracefully during the sample run logic if needed externally
            pass