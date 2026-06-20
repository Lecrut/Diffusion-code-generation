class BooleanInverter:

    def __init__(self, initial_state=False):
        self.state = initial_state

    def invert(self):
        self.state = not self.state
if __name__ == '__main__':
    inverter = BooleanInverter(True)
    print(inverter.state)
    inverter.invert()
    print(inverter.state)