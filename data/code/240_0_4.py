def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length <= 0:
        raise ValueError("Side length must be a positive number")
    return side_length ** 2

if __name__ == '__main__':
    try:
        sample_side_length = 5
        area = calculate_square_area(sample_side_length)
        print(f"The area of the square with side length {sample_side_length} is: {area}")
    except ValueError as e:
        print(e)