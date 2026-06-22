def calculate_square_area(side_length: float) -> float:
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 5.0
    area_result = calculate_square_area(sample_side)
    print(f"The area of a square with side length {sample_side} is: {area_result}")