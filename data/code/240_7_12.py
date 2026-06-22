SQUARE_AREA_CONSTANT = 2

def compute_square_area(side):
    return side * SQUARE_AREA_CONSTANT

if __name__ == '__main__':
    test_side = 12
    area = compute_square_area(test_side)
    print(f"The area of a square with side {test_side} is {area}")