class TriangleCalculator:
    BASE = 10
    HEIGHT = 5

    @staticmethod
    def calculate_area(base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base * height

if __name__ == '__main__':
    try:
        area = TriangleCalculator.calculate_area(TriangleCalculator.BASE, TriangleCalculator.HEIGHT)
        print(area)
    except ValueError as e:
        print(e)