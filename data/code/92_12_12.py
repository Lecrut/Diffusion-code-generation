class TruthValueConverter:
    TRUE_STRINGS = {'True', 'true'}
    FALSE_STRINGS = {'False', 'false'}

    @staticmethod
    def is_true(value):
        return value in TruthValueConverter.TRUE_STRINGS

    @staticmethod
    def get_opposite(value):
        if TruthValueConverter.is_true(value):
            return 'False'
        elif value in TruthValueConverter.FALSE_STRINGS:
            return 'True'
        else:
            raise ValueError("Invalid boolean string")

if __name__ == '__main__':
    converter = TruthValueConverter()
    sample1 = 'True'
    opposite1 = converter.get_opposite(sample1)
    print(f"Original: {sample1}, Opposite: {opposite1}")
    sample2 = 'false'
    opposite2 = converter.get_opposite(sample2)
    print(f"Original: {sample2}, Opposite: {opposite2}")