class BooleanNegator:
    def negate_boolean(self, value):
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate_boolean(True))
    print(negator.negate_boolean(False))