class AreaCalculator:
    def get_difference(self, area_a, area_b):
        if not (isinstance(area_a, (int, float)) and isinstance(area_b, (int, float))):
            raise ValueError("Both areas must be numbers.")
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    area1 = 25.0
    area2 = 30.0
    difference = calculator.get_difference(area1, area2)
    print(difference)