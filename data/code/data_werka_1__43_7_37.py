SQUARE_AREA_CONSTANT = 1

def calculate_square_area(side: float) -> float:
    return side * side * SQUARE_AREA_CONSTANT

if __name__ == '__main__':
    sample_side_length = 5.0
    area = calculate_square_area(sample_side_length)
    print(f"The area of the square with side {sample_side_length} is {area}")