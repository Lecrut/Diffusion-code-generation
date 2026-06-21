class BooleanInverter:
    def __init__(self):
        self.true_val = True
        self.false_val = False

    def invert(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return value ^ self.true_val

    def is_inverted(self, original, inverted):
        return inverted == self.invert(original)

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))
    print(inverter.is_inverted(True, False))
    print(inverter.is_inverted(False, True))
    print(inverter.invert(True) ^ True)
    print(inverter.invert(False) ^ True)