class NumberComparer:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def is_valid(self):
        return isinstance(self.value1, (int, float)) and isinstance(self.value2, (int, float))

    def compare(self):
        if not self.is_valid():
            raise ValueError('Both values must be integers or floats')
        return max(self.value1, self.value2)
if __name__ == '__main__':
    sample_value1 = 25.7
    sample_value2 = 40
    comparer = NumberComparer(sample_value1, sample_value2)
    print(comparer.is_valid())
    larger_value = comparer.compare()
    print(larger_value)