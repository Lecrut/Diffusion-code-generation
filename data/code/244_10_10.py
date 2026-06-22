class GeometryCalculator:
    def circle_area(self, radius):
        return 3.14159 * radius ** 2

    def rectangle_area(self, width, height):
        return width * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    circle_radius = 5
    rectangle_width = 10
    rectangle_height = 7
    total_area = calculator.circle_area(circle_radius) + calculator.rectangle_area(rectangle_width, rectangle_height)
    print(total_area)