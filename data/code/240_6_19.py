def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length <= 0:
        raise ValueError("Side length must be a positive number")
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 5.0
    area = calculate_square_area(sample_side)
    print(f"The side of the square is: {sample_side}")
    print(f"The area of the square is: {area}")