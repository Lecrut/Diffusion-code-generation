class BooleanInverter:
    def invert(self, value):
        return value ^ True

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))