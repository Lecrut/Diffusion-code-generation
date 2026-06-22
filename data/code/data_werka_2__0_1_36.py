class UnitConverter:
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / 3.28084
    METERS_TO_KILOMETERS = 0.001
    KILOMETERS_TO_METERS = 1000

    @staticmethod
    def validate_value(value):
        if not isinstance(value, (int, float)):
            raise ValueError('Value must be a number')

    @classmethod
    def convert_meters_to_feet(cls, value):
        cls.validate_value(value)
        return value * cls.METERS_TO_FEET

    @classmethod
    def convert_feet_to_meters(cls, value):
        cls.validate_value(value)
        return value * cls.FEET_TO_METERS

    @classmethod
    def convert_meters_to_kilometers(cls, value):
        cls.validate_value(value)
        return value * cls.METERS_TO_KILOMETERS

    @classmethod
    def convert_kilometers_to_meters(cls, value):
        cls.validate_value(value)
        return value * cls.KILOMETERS_TO_METERS
if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.convert_meters_to_feet(10))
    print(converter.convert_feet_to_meters(32.8084))
    print(converter.convert_meters_to_kilometers(5000))
    print(converter.convert_kilometers_to_meters(5.0))