class BooleanNegator:
    TRUE = True
    FALSE = False

    @staticmethod
    def negate_boolean(b):
        return b ^ BooleanNegator.TRUE

if __name__ == '__main__':
    print(BooleanNegator.negate_boolean(True))
    print(BooleanNegator.negate_boolean(False))