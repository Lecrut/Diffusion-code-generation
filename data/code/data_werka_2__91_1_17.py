class BooleanInverter:
    @classmethod
    def invert(cls, flag: bool) -> bool:
        if not isinstance(flag, bool):
            raise ValueError("Input must be a boolean")
        return not flag

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert(True))
    print(inverter.invert(False))