class GeometryCalculator:
    @staticmethod
    def parallelogram_area(base, height):
        return base * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    result = calculator.parallelogram_area(5, 10)
    print(result)