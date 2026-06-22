class BooleanInverter:
    def __init__(self, values):
        self.original_values = list(values)

    def invert(self):
        return [not v for v in self.original_values]

    def get_original(self):
        return self.original_values

if __name__ == '__main__':
    data = [True, False, False, True]
    inverter = BooleanInverter(data)
    print(inverter.invert())
    print(inverter.get_original())