class WeightCalculator:
    def calculate_difference(self, weight1, weight2):
        return abs(weight1 - weight2)
if __name__ == '__main__':
    calculator = WeightCalculator()
    weight_a = 75
    weight_b = 60
    difference = calculator.calculate_difference(weight_a, weight_b)
    print(difference)