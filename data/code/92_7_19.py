class BooleanInverter:
    TRUE = True
    FALSE = False

    @staticmethod
    def invert(value: bool) -> bool:
        if value is BooleanInverter.TRUE:
            return BooleanInverter.FALSE
        return BooleanInverter.TRUE

if __name__ == '__main__':
    print(BooleanInverter.invert(True))
    print(BooleanInverter.invert(False))