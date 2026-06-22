class BooleanInverter:
    TRUE_BIT: int = 0x1
    FALSE_BIT: int = 0x0

    @staticmethod
    def invert(value: bool) -> bool:
        int_val: int = 1 if value else 0
        inverted_int: int = ~int_val & BooleanInverter.TRUE_BIT
        return bool(inverted_int)

if __name__ == '__main__':
    print(BooleanInverter.invert(True))
    print(BooleanInverter.invert(False))