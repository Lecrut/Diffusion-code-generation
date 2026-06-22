class WeightConverter:
    CONVERSION_FACTORS = {'kg': 1.0, 'lb': 2.20462, 'g': 1000.0}

    @staticmethod
    def convert(value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError('Input value must be a number.')
        if from_unit not in WeightConverter.CONVERSION_FACTORS or to_unit not in WeightConverter.CONVERSION_FACTORS:
            raise ValueError('Invalid unit provided.')
        return value * (WeightConverter.CONVERSION_FACTORS[from_unit] / WeightConverter.CONVERSION_FACTORS[to_unit])
if __name__ == '__main__':
    converter = WeightConverter()
    print(converter.convert(1, 'kg', 'lb'))
    print(converter.convert(1, 'lb', 'kg'))
    print(converter.convert(1000, 'g', 'kg'))