class BooleanNegator:
    @staticmethod
    def negate(value):
        return not value

if __name__ == '__main__':
    sample_value_true = True
    print(f"Original: {sample_value_true}, Negated: {BooleanNegator.negate(sample_value_true)}")
    sample_value_false = False
    print(f"Original: {sample_value_false}, Negated: {BooleanNegator.negate(sample_value_false)}")