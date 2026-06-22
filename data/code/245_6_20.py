def rhombus_area(d1, d2):
    return d1 * d2 // 4

def square_area(side):
    return side ** 2

def equal_areas(rhombus_d1, rhombus_d2, square_side):
    return rhombus_area(rhombus_d1, rhombus_d2) == square_area(square_side)
if __name__ == '__main__':
    print(equal_areas(8, 6, 5))