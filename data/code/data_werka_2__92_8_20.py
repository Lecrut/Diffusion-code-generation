class BitwiseInverter:
    def __init__(self, mask=1):
        self.mask = mask

    def invert(self, value):
        return bool(~value & self.mask)

if __name__ == '__main__':
    inverter = BitwiseInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))