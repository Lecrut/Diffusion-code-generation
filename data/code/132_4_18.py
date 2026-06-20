class BooleanNegator:
    FALSE = False
    TRUE = True

    @staticmethod
    def negate_if_false(condition):
        return not condition
if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate_if_false(False))
    print(negator.negate_if_false(True))