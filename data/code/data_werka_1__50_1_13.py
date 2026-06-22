class AreaCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator = AreaCalculator(200, 75)
    print(calculator.calculate_difference())
    
    another_calculator = AreaCalculator(30.5, 12.8)
    print(another_calculator.calculate_difference())