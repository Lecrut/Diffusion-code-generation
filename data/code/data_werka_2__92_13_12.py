class BooleanInverter:
    MASK = True

    def __init__(self):
        self._mask = self.MASK

    def invert(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return value ^ self._mask

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))
    print(inverter.invert(True) == False)
    print(inverter.invert(False) == True)