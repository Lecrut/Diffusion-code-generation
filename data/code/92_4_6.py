class BooleanInverter:
    TRUE_STR = 'True'
    FALSE_STR = 'False'

    @staticmethod
    def invert(value: str) -> str:
        if value == BooleanInverter.TRUE_STR:
            return BooleanInverter.FALSE_STR
        if value == BooleanInverter.FALSE_STR:
            return BooleanInverter.TRUE_STR
        raise ValueError(f"Unsupported boolean string: {value}")

if __name__ == '__main__':
    print(BooleanInverter.invert('True'))
    print(BooleanInverter.invert('False'))
    print(BooleanInverter.invert('True'))
    print(BooleanInverter.invert('False'))