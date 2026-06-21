class BooleanNegator:
    def __init__(self, initial_value):
        self.current_value = initial_value

    def get_negated(self):
        return not self.current_value

    def get_original(self):
        return self.current_value

if __name__ == '__main__':
    sample_inputs = [True, False]
    for sample in sample_inputs:
        negator = BooleanNegator(sample)
        original = negator.get_original()
        negated = negator.get_negated()
        print(f"Original: {original}, Negated: {negated}")