class WeightDifferenceCalculator:
    def __init__(self):
        self.weight_pairs = {}

    def add_weight_pair(self, key, weight1, weight2):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
            raise ValueError("Weights must be numbers")
        self.weight_pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self.weight_pairs:
            raise ValueError(f'No pair found for key: {key}')
        weight1, weight2 = self.weight_pairs[key]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightDifferenceCalculator()
    calculator.add_weight_pair('example1', 45.0, 60.0)
    calculator.add_weight_pair('example2', 75, 30)
    print(calculator.get_difference('example1'))
    print(calculator.get_difference('example2'))