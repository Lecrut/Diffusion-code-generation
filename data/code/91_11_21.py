class LogicalInverter:
    def __init__(self, flag: bool):
        self.flag = flag

    def invert(self) -> bool:
        inverted_state = not self.flag
        self.flag = inverted_state
        return self.flag

if __name__ == '__main__':
    inverter = LogicalInverter(False)
    new_state = inverter.invert()
    print(new_state)
    print(inverter.flag)