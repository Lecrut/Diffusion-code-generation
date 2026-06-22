class GeometryCalculator:
    @staticmethod
    def area_parallelogram(base, height):
        return base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = GeometryCalculator.area_parallelogram(base_value, height_value)
    print(result)