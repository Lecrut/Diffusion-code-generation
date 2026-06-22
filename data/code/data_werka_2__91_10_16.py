class BooleanNegator:
    def __init__(self, flag):
        self.flag = flag

    def invert(self):
        return not self.flag

    def toggle(self):
        self.flag = not self.flag
        return self.flag

if __name__ == '__main__':
    negator_true = BooleanNegator(True)
    negator_false = BooleanNegator(False)
    print(negator_true.invert())
    print(negator_false.invert())
    print(negator_true.toggle())
    print(negator_false.toggle())