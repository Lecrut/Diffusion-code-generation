class WeightDifferenceCalculator:

    def __init__(self):
        self.weight_pairs = {}

    def add_weight_pair(self, key, weight1, weight2):
        self.weight_pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key in self.weight_pairs:
            weight1, weight2 = self.weight_pairs[key]
            return abs(weight1 - weight2)
        else:
            raise KeyError('Key not found')
if __name__ == '__main__':
    calculator = WeightDifferenceCalculator()
    calculator.add_weight_pair('pair1', 70, 65)
    calculator.add_weight_pair('pair2', 80, 75)
    print(calculator.get_difference('pair1'))
    print(calculator.get_difference('pair2'))