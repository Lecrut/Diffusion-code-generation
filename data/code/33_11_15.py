class TriangleCalculator:
    @staticmethod
    def calculate_area(base, height):
        if base <= 0:
            raise ValueError("Base must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        return 0.5 * base * height

if __name__ == '__main__':
    BASE_VAL = 12
    HEIGHT_VAL = 8
    calc = TriangleCalculator()
    print(calc.calculate_area(BASE_VAL, HEIGHT_VAL))