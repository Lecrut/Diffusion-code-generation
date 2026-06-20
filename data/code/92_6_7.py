class BooleanInverter:

    def __init__(self, initial_state: bool):
        self.state = initial_state

    def invert(self) -> bool:
        return not self.state
if __name__ == '__main__':
    inverter = BooleanInverter(True)
    print(inverter.invert())
    inverter = BooleanInverter(False)
    print(inverter.invert())