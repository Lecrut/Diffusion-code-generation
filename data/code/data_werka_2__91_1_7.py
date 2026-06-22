class BooleanInverter:
    _TRUE_VAL = True
    _FALSE_VAL = False

    @classmethod
    def invert(cls, flag: bool) -> bool:
        if flag is cls._TRUE_VAL:
            return cls._FALSE_VAL
        return cls._TRUE_VAL

if __name__ == '__main__':
    inv = BooleanInverter()
    res1 = inv.invert(True)
    res2 = inv.invert(False)
    print(res1)
    print(res2)