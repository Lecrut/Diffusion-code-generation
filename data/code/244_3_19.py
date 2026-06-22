class GeometryCalculator:
    @staticmethod
    def trapezoid_area(base1, base2, height):
        return 0.5 * (base1 + base2) * height

    @staticmethod
    def parallelogram_area(base, height):
        return base * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    trapezoid_area = calculator.trapezoid_area(5, 7, 4)
    parallelogram_area = calculator.parallelogram_area(6, 3)
    result = trapezoid_area + parallelogram_area
    print(result)