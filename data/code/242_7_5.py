class Shape:
    def area_rhombus(self, d1, d2):
        return 0.5 * d1 * d2
    
    def area_square(self, side):
        return side ** 2

if __name__ == '__main__':
    shape_calculator = Shape()
    rhombus_area = shape_calculator.area_rhombus(10, 8)
    square_area = shape_calculator.area_square(6)
    print(f"Rhombus Area: {rhombus_area}")
    print(f"Square Area: {square_area}")