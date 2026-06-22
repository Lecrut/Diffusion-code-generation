SQUARE_SIDE_LENGTH = 5.0

def calculate_square_area(side: float) -> float:
    return side * side

if __name__ == '__main__':
    area = calculate_square_area(SQUARE_SIDE_LENGTH)
    print(f"The area of the square with side {SQUARE_SIDE_LENGTH} is {area}")