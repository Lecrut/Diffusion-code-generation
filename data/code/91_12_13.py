class BooleanNegator:
    _TRUTH_TABLE = {True: False, False: True}

    @staticmethod
    def negate(value: bool) -> bool:
        return BooleanNegator._TRUTH_TABLE[value]

if __name__ == '__main__':
    print(BooleanNegator.negate(True))
    print(BooleanNegator.negate(False))