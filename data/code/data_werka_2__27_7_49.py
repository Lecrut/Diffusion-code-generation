class NumericComparer:

    def __init__(self, values):
        if not all((isinstance(v, (int, float)) for v in values.values())):
            raise ValueError('All values in the dictionary must be numeric (int or float).')
        self.values = values

    def compare(self, key1, key2):
        return self.values[key1] != self.values[key2]
if __name__ == '__main__':
    sample_values = {'number_one': 42, 'number_two': 3.14, 'number_three': 27}
    comparer = NumericComparer(sample_values)
    result1 = comparer.compare('number_one', 'number_two')
    result2 = comparer.compare('number_one', 'number_three')
    print(result1)
    print(result2)