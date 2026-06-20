class WeightCalculator:
    def __init__(self, unit='kg'):
        self.unit = unit

    def calculate_difference(self, weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightCalculator()
    result = calculator.calculate_difference(150.5, 120.0)
    print(result)
    result_kg = calculator.calculate_difference(10, 5)
    print(result_kg)