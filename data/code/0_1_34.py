class UnitConverter:
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / 3.28084
    METERS_TO_KILOMETERS = 0.001
    KILOMETERS_TO_METERS = 1000

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        if from_unit == 'meters':
            return cls._convert_from_meters(value, to_unit)
        elif from_unit == 'feet':
            return cls._convert_from_feet(value, to_unit)
        elif from_unit == 'kilometers':
            return cls._convert_from_kilometers(value, to_unit)
        else:
            raise ValueError('Unsupported unit')

    @classmethod
    def _convert_from_meters(cls, value, to_unit):
        if to_unit == 'feet':
            return value * cls.METERS_TO_FEET
        elif to_unit == 'kilometers':
            return value * cls.METERS_TO_KILOMETERS
        else:
            raise ValueError('Unsupported conversion')

    @classmethod
    def _convert_from_feet(cls, value, to_unit):
        if to_unit == 'meters':
            return value * cls.FEET_TO_METERS
        elif to_unit == 'kilometers':
            return value * cls.FEET_TO_METERS * cls.METERS_TO_KILOMETERS
        else:
            raise ValueError('Unsupported conversion')

    @classmethod
    def _convert_from_kilometers(cls, value, to_unit):
        if to_unit == 'meters':
            return value * cls.KILOMETERS_TO_METERS
        elif to_unit == 'feet':
            return value * cls.KILOMETERS_TO_METERS * cls.METERS_TO_FEET
        else:
            raise ValueError('Unsupported conversion')
if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.convert(10, 'meters', 'feet'))
    print(converter.convert(32.8084, 'feet', 'meters'))
    print(converter.convert(5000, 'meters', 'kilometers'))