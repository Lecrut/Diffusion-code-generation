class BooleanInverter:
    @staticmethod
    def invert(value: bool) -> bool:
        return not value

if __name__ == '__main__':
    sample_values = [True, False, True, False, True]
    inverted_values = [BooleanInverter.invert(val) for val in sample_values]
    print(inverted_values)