class LengthConverter:
    CONVERSIONS = {'m': 1, 'pm': 1e-12}

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in LengthConverter.CONVERSIONS or to_unit not in LengthConverter.CONVERSIONS:
            raise ValueError('Invalid unit specified')
        meters = value * LengthConverter.CONVERSIONS[from_unit]
        return meters / LengthConverter.CONVERSIONS[to_unit]
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1, 'pm', 'm'))