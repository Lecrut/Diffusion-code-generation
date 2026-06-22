class BooleanInverter:
    TRUE_VAL = 1
    FALSE_VAL = 0

    def __init__(self):
        self._lookup = {True: False, False: True}

    def invert(self, flag: bool) -> bool:
        if not isinstance(flag, bool):
            raise ValueError("Input must be a boolean")
        return self._lookup[flag]

if __name__ == '__main__':
    inverter = BooleanInverter()
    original = True
    inverted = inverter.invert(original)
    print(inverted)
    original = False
    inverted = inverter.invert(original)
    print(inverted)