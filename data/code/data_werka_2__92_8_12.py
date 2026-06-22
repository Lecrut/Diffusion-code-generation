class BitwiseInverter:
    MASK = 1

    @staticmethod
    def invert(value: bool) -> bool:
        return bool(~value & BitwiseInverter.MASK)

if __name__ == '__main__':
    inv = BitwiseInverter()
    print(inv.invert(True))
    print(inv.invert(False))