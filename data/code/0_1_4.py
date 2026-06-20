class UnitConverter:
    METERS_TO_FEET = 3.28084
    METERS_TO_KILOMETERS = 0.001
    FEET_TO_METERS = 1.0 / METERS_TO_FEET
    KILOMETERS_TO_METERS = 1.0 / METERS_TO_KILOMETERS

    @classmethod
    def meters_to_feet(cls, meters):
        return meters * cls.METERS_TO_FEET

    @classmethod
    def feet_to_meters(cls, feet):
        return feet * cls.FEET_TO_METERS

    @classmethod
    def meters_to_kilometers(cls, meters):
        return meters * cls.METERS_TO_KILOMETERS

    @classmethod
    def kilometers_to_meters(cls, kilometers):
        return kilometers * cls.KILOMETERS_TO_METERS

    @classmethod
    def feet_to_kilometers(cls, feet):
        meters = cls.feet_to_meters(feet)
        return cls.meters_to_kilometers(meters)

    @classmethod
    def kilometers_to_feet(cls, kilometers):
        meters = cls.kilometers_to_meters(kilometers)
        return cls.meters_to_feet(meters)

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.meters_to_feet(100))
    print(converter.feet_to_meters(328.084))
    print(converter.meters_to_kilometers(1500))
    print(converter.kilometers_to_meters(2.5))
    print(converter.feet_to_kilometers(1000))
    print(converter.kilometers_to_feet(5))