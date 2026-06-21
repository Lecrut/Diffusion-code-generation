class WeightDifferenceCalculator:
    def __init__(self):
        self.weight_pairs = {}

    def add_pair(self, key, weight1, weight2):
        self.weight_pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self.weight_pairs:
            raise ValueError('Key not found')
        weight1, weight2 = self.weight_pairs[key]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightDifferenceCalculator()
    calculator.add_pair('pairA', 45, 60)
    calculator.add_pair('pairB', 80, 20)
    print(calculator.get_difference('pairA'))
    print(calculator.get_difference('pairB'))