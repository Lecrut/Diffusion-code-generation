class GeometryCalculator:
    @staticmethod
    def parallelogram_area(base, height):
        return base * height

if __name__ == '__main__':
    base = 10
    height = 5
    result = GeometryCalculator.parallelogram_area(base, height)
    print(result)