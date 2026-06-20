class BooleanInverter:
    def __init__(self, initial_value: bool):
        self.value = initial_value

    def invert(self) -> None:
        self.value = not self.value

    def get_inverted_value(self) -> bool:
        return not self.value

if __name__ == '__main__':
    inverter_true = BooleanInverter(True)
    print(f"Original True: {inverter_true.get_inverted_value()}")
    inverter_true.invert()
    print(f"Inverted True to False: {inverter_true.get_inverted_value()}")

    inverter_false = BooleanInverter(False)
    print(f"Original False: {inverter_false.get_inverted_value()}")
    inverter_false.invert()
    print(f"Inverted False to True: {inverter_false.get_inverted_value()}")