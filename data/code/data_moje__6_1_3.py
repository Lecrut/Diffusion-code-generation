class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    sample1 = 50.5
    sample2 = 45.0
    calculator = WeightCalculator(sample1, sample2)
    result = calculator.calculate_difference()
    print(result)