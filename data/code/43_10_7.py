def calculate_square_area(side_length):
    """Calculates the area of a square given its side length."""
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    side_lengths = [5, 10]

    for side in side_lengths:
        area = calculate_square_area(side)
        print(f"Square with side length {side} has an area of {area}.")