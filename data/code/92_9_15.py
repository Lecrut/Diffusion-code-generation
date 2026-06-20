class BooleanInverter:
    TRUE = True
    FALSE = False

    @staticmethod
    def invert(boolean_value):
        return not boolean_value

if __name__ == '__main__':
    sample_values = [BooleanInverter.TRUE, BooleanInverter.FALSE]
    for value in sample_values:
        print(f"Original: {value}, Inverted: {BooleanInverter.invert(value)}")