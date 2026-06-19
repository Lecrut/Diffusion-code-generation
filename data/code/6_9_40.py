class WeightCalculator:
    def calculate_weight_difference(self, weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight1 = 70.5
    weight2 = 65.3
    difference = calculator.calculate_weight_difference(weight1, weight2)
    print(difference)