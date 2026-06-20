class BooleanInverter:
    TRUE = True

    @staticmethod
    def invert(value):
        return value ^ BooleanInverter.TRUE

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))