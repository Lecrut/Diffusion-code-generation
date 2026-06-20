class BooleanInverter:
    def invert(self, boolean_value: bool) -> bool:
        return not boolean_value

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))