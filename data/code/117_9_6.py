class NumberDifference:
    def __init__(self, values):
        self.values = values

    def compute_difference(self):
        return abs(self.values['a'] - self.values['b'])

if __name__ == '__main__':
    sample_values = {'a': 10, 'b': 5}
    diff_instance = NumberDifference(sample_values)
    print(diff_instance.compute_difference())