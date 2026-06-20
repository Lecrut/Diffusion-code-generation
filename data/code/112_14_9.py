class DecimalAdder:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    sample_values = {'a': 3.5, 'b': 2.7}
    result = DecimalAdder.add(sample_values['a'], sample_values['b'])
    print(result)