class BooleanNegator:

    @classmethod
    def negate(cls, value):
        if not isinstance(value, bool):
            raise ValueError('Input must be a boolean')
        return not value
if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(True))
    print(negator.negate(False))