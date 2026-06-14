def calculate_square_area(side_length: float) -> float:
    return side_length * side_length
if __name__ == '__main__':
    sample_side = 5.0
    area = calculate_square_area(sample_side)
    print(f"The area of the square with side length {sample_side} is {area}")
    sample_side_2 = 10.5
    area_2 = calculate_square_area(sample_side_2)
    print(f"The area of the square with side length {sample_side_2} is {area_2}")