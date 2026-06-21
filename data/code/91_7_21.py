class BooleanNegator:
    def __init__(self, value):
        self.value = value

    def negate(self):
        return not self.value

    def get_original(self):
        return self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    print(negator.negate())
    print(negator.get_original())