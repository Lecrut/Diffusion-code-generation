class BooleanInverter:
    def __init__(self, source):
        self.source = source

    def invert(self):
        for val in self.source:
            yield not val

    def get_list(self):
        return list(self.invert())

if __name__ == '__main__':
    data = [True, False, True, False, True]
    inverter = BooleanInverter(data)
    print(inverter.get_list())
    print(list(inverter.invert()))