import math

def get_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive prompts or input() calls.
    side_lengths = [5, "10", 3.5]

    for value in side_lengths:
        try:
            if isinstance(value, str):
                calculated_side = float(value)
            else:
                calculated_side = float(value)
            
            area = get_square_area(calculated_side)
            print(f"Side length: {calculated_side}, Area: {area}")
        except ValueError as e:
            print(f"Error processing input '{value}': Cannot convert to number.")
        except OverflowError:
            print("Input value resulted in an overflow, skipping calculation.")