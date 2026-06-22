SQUARE_AREA_CONSTANT = 1

def calculate_square_area(side: float) -> float:
    return side * side * SQUARE_AREA_CONSTANT

if __name__ == '__main__':
    sample_sides = [3.0, 5.0, 7.0]
    for side in sample_sides:
        area = calculate_square_area(side)
        print(f"The area of the square with side {side} is {area}")