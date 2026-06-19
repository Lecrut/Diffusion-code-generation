class ShapeCalculator:
    BASE_MULTIPLIER = 0.5

    @staticmethod
    def calculate_area(base, height):
        return ShapeCalculator.BASE_MULTIPLIER * base * height

if __name__ == '__main__':
    sample_base = 7.0
    sample_height = 4.0
    result = ShapeCalculator.calculate_area(sample_base, sample_height)
    print(result)