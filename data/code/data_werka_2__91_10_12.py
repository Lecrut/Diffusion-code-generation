def negate_boolean(value):
    return not value

class BooleanNegator:
    def __init__(self, initial):
        self.value = initial

    def get_negated(self):
        return not self.value

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))
    negator = BooleanNegator(True)
    print(negator.get_negated())
    negator.value = False
    print(negator.get_negated())