def calculate_square_area(side_length: float) -> float:
    if not isinstance(side_length, (int, float)):
        raise TypeError("side length must be a number")
    return side_length ** 2

if __name__ == '__main__':
    try:
        sample_side = 5.0
        area_result = calculate_square_area(sample_side)
        print(f"The area of a square with side length {sample_side} is: {area_result}")
    except TypeError as e:
        print(e)