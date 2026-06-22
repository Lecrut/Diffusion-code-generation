class GeometryCalculator:
    @staticmethod
    def parallelogram_area(base, height):
        return base * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    area = calculator.parallelogram_area(10, 5)
    print(area)