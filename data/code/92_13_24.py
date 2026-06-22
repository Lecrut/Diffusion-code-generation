class BooleanInverter:
    INVERT_MAP = {True: False, False: True}

    @staticmethod
    def invert(value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return value ^ True

if __name__ == '__main__':
    print(BooleanInverter.invert(True))
    print(BooleanInverter.invert(False))