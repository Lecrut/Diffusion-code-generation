class LengthConverter:
    CONVERSION_FACTORS = {
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit not in LengthConverter.CONVERSION_FACTORS or to_unit not in LengthConverter.CONVERSION_FACTORS:
            raise ValueError('Unsupported unit')
        value_in_meters = value * LengthConverter.CONVERSION_FACTORS[from_unit]
        converted_value = value_in_meters / LengthConverter.CONVERSION_FACTORS[to_unit]
        return converted_value

if __name__ == '__main__':
    length_value = 150
    from_unit = 'mm'
    to_unit = 'cm'
    converter = LengthConverter()
    converted_length = converter.convert(length_value, from_unit, to_unit)
    print(converted_length)