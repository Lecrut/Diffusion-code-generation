class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    calculator = WeightCalculator(100.5, 85.2)
    result = calculator.calculate_difference()
    print(result)