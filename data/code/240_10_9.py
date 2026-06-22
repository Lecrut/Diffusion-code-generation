def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return side_length * side_length

if __name__ == '__main__':
    sample_side = 5
    try:
        area = calculate_square_area(sample_side)
        print(f"The area of the square with side {sample_side} is: {area}")
    except ValueError as e:
        print(f"Error: Invalid input. {e}")