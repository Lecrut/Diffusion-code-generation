class AreaCalculator:
    def get_difference(self, area_a, area_b):
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    area_a = 25.0
    area_b = 10.0
    difference = calculator.get_difference(area_a, area_b)
    print(difference)