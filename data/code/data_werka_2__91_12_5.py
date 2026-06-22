class BooleanNegator:
    _TRUE = True
    _FALSE = False

    @staticmethod
    def negate(value):
        if value is BooleanNegator._TRUE:
            return BooleanNegator._FALSE
        return BooleanNegator._TRUE

if __name__ == '__main__':
    result_true = BooleanNegator.negate(True)
    result_false = BooleanNegator.negate(False)
    print(result_true)
    print(result_false)