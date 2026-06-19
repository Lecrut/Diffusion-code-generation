class AreaCalculator:
    @staticmethod
    def calculate_difference(area1, area2):
        return abs(area1 - area2)

if __name__ == '__main__':
    area_value1 = 200.5
    area_value2 = 75.3
    calculator = AreaCalculator()
    difference = calculator.calculate_difference(area_value1, area_value2)
    print(difference)