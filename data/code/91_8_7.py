class BooleanNegator:
    TRUE_VALUE = True
    FALSE_VALUE = False

    @staticmethod
    def negate(value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    test_values = [True, False]
    for val in test_values:
        result = negator.negate(val)
        print(f"Original: {val}, Negated: {result}")