class BooleanInverter:

    def __init__(self, initial_value):
        self.value = initial_value

    def invert(self):
        self.value = not self.value
        return self.value
if __name__ == '__main__':
    inverter = BooleanInverter(True)
    print(inverter.invert())
    print(inverter.invert())