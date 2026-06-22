def validate_side_length(side_length: float) -> bool:
    return isinstance(side_length, (int, float)) and side_length >= 0

def calculate_square_area(side_length: float) -> float:
    if not validate_side_length(side_length):
        raise ValueError("Side length must be a non-negative number")
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 7.5
    try:
        area_result = calculate_square_area(sample_side)
        print(f"The area of a square with side length {sample_side} is: {area_result}")
    except ValueError as e:
        print(e)