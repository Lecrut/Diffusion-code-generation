class BooleanNegator:
    _NEGATION_MAP = {True: False, False: True}

    @staticmethod
    def negate(value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return BooleanNegator._NEGATION_MAP[value]

if __name__ == '__main__':
    print(BooleanNegator.negate(True))
    print(BooleanNegator.negate(False))