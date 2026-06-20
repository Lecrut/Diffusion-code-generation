class WeightCalculator:
    def __init__(self, unit='kg'):
        self.unit = unit

    def calculate_difference(self, weight1, weight2):
        return abs(weight1 - weight2)

    def calculate_difference_with_sign(self, weight1, weight2):
        return weight1 - weight2

if __name__ == '__main__':
    calculator = WeightCalculator()
    w1 = 85.5
    w2 = 70.2
    diff = calculator.calculate_difference(w1, w2)
    signed_diff = calculator.calculate_difference_with_sign(w1, w2)
    print(diff)
    print(signed_diff)