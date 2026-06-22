class UnitConverter:
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / 3.28084
    METERS_TO_KILOMETERS = 0.001
    KILOMETERS_TO_METERS = 1000.0

    @classmethod
    def meters_to_feet(cls, value):
        return value * cls.METERS_TO_FEET

    @classmethod
    def feet_to_meters(cls, value):
        return value * cls.FEET_TO_METERS

    @classmethod
    def meters_to_kilometers(cls, value):
        return value * cls.METERS_TO_KILOMETERS

    @classmethod
    def kilometers_to_meters(cls, value):
        return value * cls.KILOMETERS_TO_METERS

    @classmethod
    def feet_to_kilometers(cls, value):
        meters = cls.feet_to_meters(value)
        return cls.meters_to_kilometers(meters)

    @classmethod
    def kilometers_to_feet(cls, value):
        meters = cls.kilometers_to_meters(value)
        return cls.meters_to_feet(meters)

if __name__ == '__main__':
    converter = UnitConverter()

    print(converter.meters_to_feet(10))
    print(converter.feet_to_meters(32.8084))
    print(converter.meters_to_kilometers(5000))
    print(converter.kilometers_to_meters(2))
    print(converter.feet_to_kilometers(1000))
    print(converter.kilometers_to_feet(1))