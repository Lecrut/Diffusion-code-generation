def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Side length must be a non-negative number")
    return float(side_length ** 2)

if __name__ == '__main__':
    try:
        area = calculate_square_area(5)
        print(f"The area of the square is: {area:.4f}")
    except ValueError as e:
        print(e)