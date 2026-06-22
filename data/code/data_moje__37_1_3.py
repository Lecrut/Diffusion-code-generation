class GeometryCalculator:
    @staticmethod
    def calculate_parallelogram_area(base, height):
        return base * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    result = calculator.calculate_parallelogram_area(10, 5)
    print(result)