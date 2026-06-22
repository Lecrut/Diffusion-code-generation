class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_absolute_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    weight_a = 80.5
    weight_b = 72.3
    calculator = WeightCalculator(weight_a, weight_b)
    difference = calculator.calculate_absolute_difference()
    print(difference)