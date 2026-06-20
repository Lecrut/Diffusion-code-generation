class BooleanNegator:
    def negate(self, value: bool) -> bool:
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    sample_value_true = True
    print(f"Original: {sample_value_true}, Negated: {negator.negate(sample_value_true)}")
    sample_value_false = False
    print(f"Original: {sample_value_false}, Negated: {negator.negate(sample_value_false)}")