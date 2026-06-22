class BooleanInverter:
    def __init__(self, initial_value: bool = False):
        self.value = initial_value

    def invert(self) -> bool:
        self.value = not self.value
        return self.value

    def get_value(self) -> bool:
        return self.value

if __name__ == '__main__':
    inverter = BooleanInverter(initial_value=True)
    print(inverter.invert())
    print(inverter.get_value())
    inverter.value = False
    print(inverter.invert())
    print(inverter.get_value())