class BooleanNegator:
    @staticmethod
    def negate_boolean(value):
        return not value

if __name__ == '__main__':
    original_value = True
    negated_value = BooleanNegator.negate_boolean(original_value)
    print(f"Original value: {original_value}")
    print(f"Negated value: {negated_value}")