def area_rhombus(d1, d2):
    return 0.5 * d1 * d2

def area_square(side):
    return side ** 2

if __name__ == '__main__':
    rhombus_area = area_rhombus(12, 6)
    square_area = area_square(7)
    print(f"Rhombus Area: {rhombus_area}")
    print(f"Square Area: {square_area}")