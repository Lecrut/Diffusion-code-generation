def calculate_square_area(side_length):
    """Calculates the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Sample inputs to demonstrate functionality without user interaction or external dependencies.
    sample_inputs = [3, -1]

    for s in sample_inputs:
        try:
            if not isinstance(s, (int, float)):
                raise TypeError("Side length must be a number.")
            
            area_result = calculate_square_area(s)
            
            # If the side is negative, output an error message instead of a positive area.
            if s < 0 and isinstance(s, int):
                print(f"Error: Side length cannot be negative for {s}.")
            else:
                print(f"The square with side length {s} has an area of: {area_result}")

        except (TypeError, ValueError) as e:
            # Handles cases where input is not a number or conversion fails.
            if isinstance(e, TypeError):
                print("Error occurred while processing the sample value.", type(e).__name__)
            else:
                raise