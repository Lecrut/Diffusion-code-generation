class GeometryCalculator:
    BASE_VALUE = 7
    HEIGHT_VALUE = 4

    @staticmethod
    def compute_area(base, height):
        return base * height

if __name__ == '__main__':
    base = GeometryCalculator.BASE_VALUE
    height = GeometryCalculator.HEIGHT_VALUE
    print(GeometryCalculator.compute_area(base, height))