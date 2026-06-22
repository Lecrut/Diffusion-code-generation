class GeometryCalculator:
    @staticmethod
    def area_of_parallelogram(base, height):
        return base * height

if __name__ == '__main__':
    calc = GeometryCalculator()
    base = 10
    height = 5
    result = calc.area_of_parallelogram(base, height)
    print(result)