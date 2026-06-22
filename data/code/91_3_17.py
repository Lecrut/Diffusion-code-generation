class BooleanInverter:
    _TRUE_BIT: int = 0x1
    _FALSE_BIT: int = 0x0

    @staticmethod
    def invert(value: bool) -> bool:
        int_val: int = 1 if value else 0
        flipped_int: int = int_val ^ BooleanInverter._TRUE_BIT
        return bool(flipped_int)

if __name__ == '__main__':
    print(BooleanInverter.invert(True))
    print(BooleanInverter.invert(False))