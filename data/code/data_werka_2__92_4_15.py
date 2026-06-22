class BooleanInverter:
    TRUE_STR = 'True'
    FALSE_STR = 'False'

    def invert(self, value: str) -> str:
        if value == self.TRUE_STR:
            return self.FALSE_STR
        if value == self.FALSE_STR:
            return self.TRUE_STR
        raise ValueError(f"Unsupported boolean string: {value}")

if __name__ == '__main__':
    inverter = BooleanInverter()
    print(inverter.invert('True'))
    print(inverter.invert('False'))