class UnitConverter:
    CONVERSION_FACTOR = {
        ('gram', 'ounce'): 0.035274
    }

    @staticmethod
    def convert(value):
        from_unit, to_unit = value.split()
        key = (from_unit, to_unit)
        if key in UnitConverter.CONVERSION_FACTOR:
            return round(value[2] * UnitConverter.CONVERSION_FACTOR[key], 4)
        else:
            return "Conversion not supported for this pair."

if __name__ == '__main__':
    sample_value = ('gram', 'ounce', 100)
    result = UnitConverter.convert(sample_value)
    print(result)