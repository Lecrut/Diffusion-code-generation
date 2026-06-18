import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to satisfy requirements without user input or arguments.
    # Simulating robust input handling by testing with predefined strings that need conversion.
    
    test_cases = [
        "5",      # Valid integer string
        "-3.5",   # Negative float (valid mathematically, though side length is usually positive)
        "10"
    ]

    for value_str in test_cases:
        try:
            # Robust conversion attempt using ValueError handling
            side = float(value_str)
            
            if side < 0:
                print(f"Ignoring negative side length {side}.")
                continue
                
            area = calculate_square_area(side)
            print(f"Side length: {value_str}, Area: {area}")

        except ValueError as e:
            # Handles cases where input is not a valid number, simulating robustness.
            print(f"Error converting '{value_str}' to float: {e}.")