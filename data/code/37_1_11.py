class GeometryCalculator:
    @staticmethod
    def area_of_parallelogram(base, height):
        return base * height

if __name__ == '__main__':
    base = 5
    height = 10
    result = GeometryCalculator.area_of_parallelogram(base, height)
    print(result)