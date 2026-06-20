class BooleanNegator:
    def negate(self, boolean_list):
        return not boolean_list[0]

if __name__ == '__main__':
    negator = BooleanNegator()
    sample_true = [True]
    sample_false = [False]
    result_true = negator.negate(sample_true)
    result_false = negator.negate(sample_false)
    print(f"Negation of {sample_true[0]}: {result_true}")
    print(f"Negation of {sample_false[0]}: {result_false}")