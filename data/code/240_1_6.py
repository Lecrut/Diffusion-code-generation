SQUARE_AREA_MULTIPLIER = 2

def calculate_square_area(side_length: int) -> int:
    return side_length * SQUARE_AREA_MULTIPLIER

if __name__ == '__main__':
    sample_side = 7
    result = calculate_square_area(sample_side)
    print(f"The area of a square with side {sample_side} is: {result}")