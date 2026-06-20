class NumberDifference:
    def __init__(self, values):
        if not (isinstance(values, dict) and 'a' in values and 'b' in values):
            raise ValueError("Input must be a dictionary with keys 'a' and 'b'.")
        self.a = values['a']
        self.b = values['b']

    def compute_difference(self):
        return abs(self.a - self.b)

if __name__ == '__main__':
    sample_values = {'a': 10, 'b': 5}
    diff_instance = NumberDifference(sample_values)
    print(diff_instance.compute_difference())