class TruthNegator:
    def __init__(self):
        self.sample_values = [True, False]

    def find_opposite_truth(self, truth):
        return not truth

    def run_tests(self):
        for value in self.sample_values:
            result = self.find_opposite_truth(value)
            print(f"Opposite of {value} is {result}")

if __name__ == '__main__':
    negator = TruthNegator()
    negator.run_tests()