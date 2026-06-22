class AreaCalculator:
    MULTIPLIER = 1

    @staticmethod
    def calculate_area(width, height):
        return width * height

if __name__ == '__main__':
    sample_width = 7
    sample_height = 3
    calculator = AreaCalculator()
    area_result = calculator.calculate_area(sample_width, sample_height)
    print(area_result)