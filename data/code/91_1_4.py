class BooleanNegator:
    @staticmethod
    def negate(value: bool) -> bool:
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(True))
    print(negator.negate(False))