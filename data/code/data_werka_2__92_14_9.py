class BooleanInverter:
    def __init__(self):
        self.opposite_map = {True: False, False: True}

    def invert(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return self.opposite_map[value]

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))
    print(inverter.invert(not True))
    print(inverter.invert(not False))