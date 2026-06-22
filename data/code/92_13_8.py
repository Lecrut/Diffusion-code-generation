class BooleanInverter:
    def __init__(self):
        self._true = True
        self._false = False

    def invert(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return value ^ self._true

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))
    print(inverter.invert(True) == False)
    print(inverter.invert(False) == True)
    print(inverter._true)
    print(inverter._false)