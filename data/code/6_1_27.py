class WeightCalculator:
    def calculate_difference(self, weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    result = calculator.calculate_difference(70.5, 68.2)
    print(result)