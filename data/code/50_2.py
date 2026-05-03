class AreaCalculator:
    def calculate_difference(self, area1, area2):
        return area1 - area2
if __name__ == '__main__':
    calculator = AreaCalculator()
    area_a = 150
    area_b = 75
    difference = calculator.calculate_difference(area_a, area_b)
    print(difference)