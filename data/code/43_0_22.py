def calculate_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("The side length must be a number.")
    if side < 0:
        raise ValueError("The side length cannot be negative.")
    return side * side

if __name__ == '__main__':
    try:
        sample_side = 7
        area_result = calculate_square_area(sample_side)
        print(f"The area of the square with side length {sample_side} is {area_result}.")
    except (TypeError, ValueError) as e:
        print(e)