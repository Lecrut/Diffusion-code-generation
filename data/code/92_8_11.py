class BooleanInverter:

    def __init__(self, value):
        self.value = value

    def invert(self):
        return not self.value
if __name__ == '__main__':
    inverter_true = BooleanInverter(True)
    print(inverter_true.invert())
    inverter_false = BooleanInverter(False)
    print(inverter_false.invert())