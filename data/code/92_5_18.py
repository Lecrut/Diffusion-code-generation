class BooleanInverter:
    def __init__(self, iterable):
        self.iterable = iterable

    def invert(self):
        for value in self.iterable:
            yield not value

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    inverter = BooleanInverter(sample_values)
    inverted_values = list(inverter.invert())
    print(inverted_values)