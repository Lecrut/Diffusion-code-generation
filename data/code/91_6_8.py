class BooleanNegator:
    def negate(self, value):
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(True))
    print(negator.negate(False))