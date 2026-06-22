class ShapeCalculator:
    def calculate_area_rectangle(self, width, height):
        return width * height

    def calculate_area_triangle(self, base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = ShapeCalculator()
    rectangle_area = calculator.calculate_area_rectangle(10, 6)
    triangle_area = calculator.calculate_area_triangle(8, 5)
    total_area = rectangle_area + triangle_area
    print(total_area)