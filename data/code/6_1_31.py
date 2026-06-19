class WeightCalculator:
    def calculate_difference(self, weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight1 = 80.5
    weight2 = 75.3
    difference = calculator.calculate_difference(weight1, weight2)
    print(difference)