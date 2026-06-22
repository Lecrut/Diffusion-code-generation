class WeightCalculator:
    def __init__(self, weight_a, weight_b):
        self.weight_a = float(weight_a)
        self.weight_b = float(weight_b)

    def calculate_difference(self):
        return abs(self.weight_a - self.weight_b)

if __name__ == '__main__':
    calc = WeightCalculator(150, 120)
    result = calc.calculate_difference()
    print(result)