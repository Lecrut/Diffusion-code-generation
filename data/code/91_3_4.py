class BooleanInverter:
    @staticmethod
    def invert(value: bool) -> bool:
        return not value

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))