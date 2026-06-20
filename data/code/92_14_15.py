class BooleanInverter:
    TRUE = True
    FALSE = False

    def invert(self, value):
        return value ^ self.TRUE

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))