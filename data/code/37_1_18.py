class GeometryCalculator:
    BASE_SCALE_FACTOR = 1
    HEIGHT_SCALE_FACTOR = 1

    @staticmethod
    def _compute_product(a, b):
        return a * b

    @staticmethod
    def area_of_parallelogram(base, height):
        scaled_base = base * GeometryCalculator.BASE_SCALE_FACTOR
        scaled_height = height * GeometryCalculator.HEIGHT_SCALE_FACTOR
        return GeometryCalculator._compute_product(scaled_base, scaled_height)

if __name__ == '__main__':
    sample_base = 15
    sample_height = 8
    calculated_area = GeometryCalculator.area_of_parallelogram(sample_base, sample_height)
    print(calculated_area)