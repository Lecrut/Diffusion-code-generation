class AreaDifferenceCalculator:
    def __init__(self):
        self.difference = 0

    def compute_difference(self, area1, area2):
        self.difference = abs(area1 - area2)
        return self.difference

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator()
    area_a = 120
    area_b = 80
    difference = calculator.compute_difference(area_a, area_b)
    print(f"Difference between {area_a} and {area_b}: {difference}")

    area_c = 75.5
    area_d = 49.5
    difference = calculator.compute_difference(area_c, area_d)
    print(f"Difference between {area_c} and {area_d}: {difference}")