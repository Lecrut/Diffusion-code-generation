def calculate_square_side_length(area):
    if not isinstance(area, (int, float)):
        raise TypeError("Area must be a number")
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    try:
        area = 25.0
        side_length = calculate_square_side_length(area)
        print(f"The side length of the square is: {side_length}")
    except (TypeError, ValueError) as e:
        print(e)