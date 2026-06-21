class BitwiseInverter:
    OPPOSITE_MASK = 1

    @staticmethod
    def invert(flag_value):
        return bool(~flag_value & BitwiseInverter.OPPOSITE_MASK)

if __name__ == '__main__':
    inverter = BitwiseInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))