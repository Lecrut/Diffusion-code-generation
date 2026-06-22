class AreaDifferenceCalculator:
    DEFAULT_AREA1 = 200
    DEFAULT_AREA2 = 100

    @staticmethod
    def calculate_difference(area1, area2):
        return area1 - area2

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator()
    area_a = 300
    area_b = 150
    difference = calculator.calculate_difference(area_a, area_b)
    print(difference)