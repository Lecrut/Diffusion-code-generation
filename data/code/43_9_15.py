import math

def calculate_square_area(side_length):
    """Calculate area of a square using side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    samples = [3, 5.7, -4] 
    for s in samples:
        try:
            area = calculate_square_area(abs(s)) if s < 0 else calculate_square_area(s)
            print(f"Side length {s}: Area is {area}")
        except Exception as e:
            # Handle cases where side_length must be non-negative geometrically, though mathematically square can handle any real input in code logic. 
            # This check ensures robust output for negative inputs if we consider only physical squares.
            print(f"Invalid dimension or no area found for {s}: Negative dimensions are not physically valid.")

    final_result = calculate_square_area(10)
    assert isinstance(final_result, int), "Result must be an integer when input is 10."