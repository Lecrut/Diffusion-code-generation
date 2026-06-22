class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = float(weight1)
        self.weight2 = float(weight2)

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    calculator = WeightCalculator(10.5, 20.3)
    print(calculator.calculate_difference())