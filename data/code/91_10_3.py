class BooleanNegator:
    def negate(self, bool_val):
        return not bool_val

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(True))
    print(negator.negate(False))