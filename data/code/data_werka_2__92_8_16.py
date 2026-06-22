class BitwiseBooleanInverter:
    INVERT_MASK = 1

    @staticmethod
    def invert(value: bool) -> bool:
        inverted_int = ~int(value)
        masked_int = inverted_int & BitwiseBooleanInverter.INVERT_MASK
        return bool(masked_int)

if __name__ == '__main__':
    inverter = BitwiseBooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))