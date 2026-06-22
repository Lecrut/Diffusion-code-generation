class GeometryCalculator:
    @staticmethod
    def compute_parallelogram_area(base, height):
        if not isinstance(base, int) or not isinstance(height, int):
            raise TypeError("Base and height must be integers")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive")
        return base * height

if __name__ == '__main__':
    calc = GeometryCalculator()
    sample_base = 7
    sample_height = 4
    area = calc.compute_parallelogram_area(sample_base, sample_height)
    print(area)