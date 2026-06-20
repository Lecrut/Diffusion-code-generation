class BooleanNegator:
    def negate(self, boolean_list):
        return not boolean_list[0]

if __name__ == '__main__':
    negator = BooleanNegator()
    sample_value = [True]
    result = negator.negate(sample_value)
    print(f"Negation of {sample_value[0]}: {result}")