class BooleanInverter:
    def __init__(self):
        self._truth_table = {True: False, False: True}

    def invert(self, flag: bool) -> bool:
        if not isinstance(flag, bool):
            raise ValueError("Input must be a boolean")
        return self._truth_table[flag]

def find_opposite_truth(value: bool) -> bool:
    inverter = BooleanInverter()
    return inverter.invert(value)

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))
    print(find_opposite_truth(True))
    print(find_opposite_truth(False))