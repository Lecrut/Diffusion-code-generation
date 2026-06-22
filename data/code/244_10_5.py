class GeometryCalculator:
    PI = 3.14159

    @staticmethod
    def circle_area(radius):
        return GeometryCalculator.PI * radius ** 2

    @staticmethod
    def rectangle_area(width, height):
        return width * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    circle_radius = 5
    rectangle_width = 10
    rectangle_height = 7
    total_area = calculator.circle_area(circle_radius) + calculator.rectangle_area(rectangle_width, rectangle_height)
    print(total_area)