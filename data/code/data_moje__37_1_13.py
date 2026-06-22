class GeometryCalculator:
    @staticmethod
    def parallelogram_area(base, height):
        if base <= 0:
            raise ValueError("Base must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        return base * height

if __name__ == '__main__':
    base = 12
    height = 4
    area = GeometryCalculator.parallelogram_area(base, height)
    print(area)