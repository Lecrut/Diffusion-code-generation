def area_rhombus(d1, d2):
    return 0.5 * d1 * d2

def area_square(side):
    return side ** 2

if __name__ == '__main__':
    rhombus_area = area_rhombus(10, 8)
    square_area = area_square(6)
    print("Rhombus Area:", rhombus_area)
    print("Square Area:", square_area)