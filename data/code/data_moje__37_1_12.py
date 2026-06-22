class GeometryCalculator:
    @staticmethod
    def calculate_parallelogram_area(base, height):
        return base * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    base = 10
    height = 5
    print(calculator.calculate_parallelogram_area(base, height))