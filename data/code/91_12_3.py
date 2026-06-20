class BooleanNegator:
    @staticmethod
    def negate(value: bool) -> bool:
        return not value

if __name__ == '__main__':
    print(BooleanNegator.negate(True))
    print(BooleanNegator.negate(False))