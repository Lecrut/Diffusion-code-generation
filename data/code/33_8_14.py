class TriangleCalculator:
    _AREA_MULTIPLIER = 0.5

    @staticmethod
    def calculate_area(base, height):
        compute = lambda b, h: b * h * TriangleCalculator._AREA_MULTIPLIER
        return compute(base, height)

if __name__ == '__main__':
    base_val = 8.5
    height_val = 12.0
    area_val = TriangleCalculator.calculate_area(base_val, height_val)
    print(area_val)