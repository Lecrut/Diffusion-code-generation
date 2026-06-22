class WeightCalculator:
    def __init__(self):
        self.history = []

    def calculate_difference(self, first_weight, second_weight):
        diff = abs(first_weight - second_weight)
        self.history.append(diff)
        return diff

if __name__ == '__main__':
    calculator = WeightCalculator()
    value_one = 85.5
    value_two = 72.3
    result = calculator.calculate_difference(value_one, value_two)
    print(result)