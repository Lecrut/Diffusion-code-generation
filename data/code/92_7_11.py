class BooleanInverter:
    TRUTH_TABLE = {True: False, False: True}

    @staticmethod
    def invert(value: bool) -> bool:
        return BooleanInverter.TRUTH_TABLE[value]

if __name__ == '__main__':
    result_true = BooleanInverter.invert(True)
    result_false = BooleanInverter.invert(False)
    print(result_true)
    print(result_false)