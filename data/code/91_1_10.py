class BooleanInverter:
    _NEGATION_MAP = {True: False, False: True}

    @classmethod
    def invert(cls, flag: bool) -> bool:
        return cls._NEGATION_MAP[flag]

if __name__ == '__main__':
    inv = BooleanInverter()
    print(inv.invert(True))
    print(inv.invert(False))