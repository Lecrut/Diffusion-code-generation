class BooleanNegator:
    def __init__(self, value):
        self.value = value

    def negate(self):
        return not self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    print(negator.negate())
    negator2 = BooleanNegator(False)
    print(negator2.negate())