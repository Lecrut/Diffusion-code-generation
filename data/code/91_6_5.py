class BooleanNegator:
    @staticmethod
    def negate(value):
        return not value

if __name__ == '__main__':
    sample_value = True
    negated_value = BooleanNegator.negate(sample_value)
    print(negated_value)