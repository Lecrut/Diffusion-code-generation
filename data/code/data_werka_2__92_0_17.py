class BooleanInverter:
    def __init__(self, initial_state: bool = False):
        self.state = initial_state

    def invert(self) -> bool:
        self.state = not self.state
        return self.state

if __name__ == '__main__':
    inverter = BooleanInverter(initial_state=True)
    result = inverter.invert()
    print(result)
    result = inverter.invert()
    print(result)