class Shape:
    PI = 3.141592653589793

    @staticmethod
    def calculate_circle_area(radius):
        return Shape.PI * radius ** 2

    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

def main():
    circle_radius = 5
    rectangle_length = 4
    rectangle_width = 6

    circle_area = Shape.calculate_circle_area(circle_radius)
    rectangle_area = Shape.calculate_rectangle_area(rectangle_length, rectangle_width)

    print(f"Circle area with radius {circle_radius}: {circle_area}")
    print(f"Rectangle area with length {rectangle_length} and width {rectangle_width}: {rectangle_area}")

if __name__ == '__main__':
    main()