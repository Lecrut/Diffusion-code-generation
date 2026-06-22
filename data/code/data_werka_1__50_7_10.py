class AreaCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_area_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator = AreaCalculator(80.75, 45.2)
    difference = calculator.calculate_area_difference()
    print(difference)