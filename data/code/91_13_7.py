class BooleanNegator:
    TRUE = True
    FALSE = False

    @staticmethod
    def negate_boolean(b):
        return b ^ BooleanNegator.TRUE

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate_boolean(True))
    print(negator.negate_boolean(False))