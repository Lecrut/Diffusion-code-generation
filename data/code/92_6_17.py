class TruthInverter:

    def __init__(self):
        self.current_state = False

    def invert(self) -> bool:
        self.current_state = not self.current_state
        return self.current_state
if __name__ == '__main__':
    inverter = TruthInverter()
    print(inverter.invert())
    print(inverter.invert())
    print(inverter.invert())