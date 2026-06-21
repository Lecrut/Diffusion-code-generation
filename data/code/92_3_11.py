class BooleanInverter:
    OPPOSITE_MAP = {True: False, False: True}

    @staticmethod
    def invert(value):
        return BooleanInverter.OPPOSITE_MAP[value]

    @classmethod
    def invert_list(cls, values):
        return [cls.invert(v) for v in values]

if __name__ == '__main__':
    sample = [True, False, True, False, True]
    result = BooleanInverter.invert_list(sample)
    print(result)