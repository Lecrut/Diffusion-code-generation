SQUARE_AREA_CONSTANT = 12

def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    area = calculate_square_area(SQUARE_AREA_CONSTANT)
    print(f"The area of a square with side {SQUARE_AREA_CONSTANT} is: {area}")