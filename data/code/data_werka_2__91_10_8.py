class BooleanNegator:
    def __init__(self):
        self.TRUTH_TABLE = {True: False, False: True}

    def negate(self, value):
        if not isinstance(value, bool):
            raise ValueError("Expected a boolean value")
        return self.TRUTH_TABLE[value]

    def toggle_state(self, state):
        return self.negate(state)

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(True))
    print(negator.negate(False))
    print(negator.toggle_state(True))
    print(negator.toggle_state(False))