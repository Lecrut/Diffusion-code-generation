def area_rhombus(d1, d2):
    return 0.5 * d1 * d2

def area_square(side):
    return side ** 2

if __name__ == '__main__':
    rhombus_d1 = 12
    rhombus_d2 = 8
    square_side = 7
    
    rhombus_area = area_rhombus(rhombus_d1, rhombus_d2)
    square_area = area_square(square_side)
    
    print(f"Rhombus Area: {rhombus_area}")
    print(f"Square Area: {square_area}")