class BooleanInverter:

    def __init__(self, initial_state=False):
        self.state = initial_state

    def invert(self):
        self.state = not self.state
        return self.state
if __name__ == '__main__':
    inverter = BooleanInverter(True)
    print(inverter.invert())
    print(inverter.invert())