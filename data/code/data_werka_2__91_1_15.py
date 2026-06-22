class BooleanInverter:
    @staticmethod
    def invert(flag: bool) -> bool:
        return not flag

if __name__ == '__main__':
    print(BooleanInverter.invert(True))
    print(BooleanInverter.invert(False))