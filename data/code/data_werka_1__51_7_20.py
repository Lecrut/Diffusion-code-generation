class MeasurementUtils:
    PI = 3.14159

    @staticmethod
    def calculate_perimeter(length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")
        return 2 * (length + width)

    @staticmethod
    def calculate_circle_circumference(radius):
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        return 2 * MeasurementUtils.PI * radius

if __name__ == '__main__':
    rectangle_length = 8
    rectangle_width = 6
    circle_radius = 5

    try:
        rectangle_perimeter = MeasurementUtils.calculate_perimeter(rectangle_length, rectangle_width)
        circle_circumference = MeasurementUtils.calculate_circle_circumference(circle_radius)

        print("Rectangle Perimeter:", rectangle_perimeter)
        print("Circle Circumference:", circle_circumference)
    except ValueError as e:
        print(e)