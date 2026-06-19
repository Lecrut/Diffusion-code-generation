class AreaDifferenceCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator1 = AreaDifferenceCalculator(75, 40)
    difference1 = calculator1.calculate_difference()
    print(f"The difference between {calculator1.area1} and {calculator1.area2} is: {difference1}")

    calculator2 = AreaDifferenceCalculator(200.5, 180.3)
    difference2 = calculator2.calculate_difference()
    print(f"The difference between {calculator2.area1} and {calculator2.area2} is: {difference2}")

    calculator3 = AreaDifferenceCalculator(500, 500)
    difference3 = calculator3.calculate_difference()
    print(f"The difference between {calculator3.area1} and {calculator3.area2} is: {difference3}")