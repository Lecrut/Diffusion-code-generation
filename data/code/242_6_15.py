class PolygonAreaCalculator:
    @staticmethod
    def calculate_trapezoid_area(base1, base2, height):
        return ((base1 + base2) * height) / 2

    @staticmethod
    def calculate_circle_area(diameter):
        radius = diameter / 2
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    trapezoid_base1 = 6
    trapezoid_base2 = 8
    trapezoid_height = 4
    circle_diameter = 5

    trapezoid_area = PolygonAreaCalculator.calculate_trapezoid_area(trapezoid_base1, trapezoid_base2, trapezoid_height)
    circle_area = PolygonAreaCalculator.calculate_circle_area(circle_diameter)

    print(f"Trapezoid area: {trapezoid_area}")
    print(f"Circle area: {circle_area}")