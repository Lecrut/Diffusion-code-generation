class UnitConverter:
    METERS_TO_FEET = 3.28084
    METERS_TO_KILOMETERS = 0.001
    FEET_TO_METERS = 0.3048
    FEET_TO_KILOMETERS = 0.0003048
    KILOMETERS_TO_METERS = 1000.0
    KILOMETERS_TO_FEET = 3280.84

    @classmethod
    def meters_to_feet(cls, meters):
        return meters * cls.METERS_TO_FEET

    @classmethod
    def meters_to_kilometers(cls, meters):
        return meters * cls.METERS_TO_KILOMETERS

    @classmethod
    def feet_to_meters(cls, feet):
        return feet * cls.FEET_TO_METERS

    @classmethod
    def feet_to_kilometers(cls, feet):
        return feet * cls.FEET_TO_KILOMETERS

    @classmethod
    def kilometers_to_meters(cls, kilometers):
        return kilometers * cls.KILOMETERS_TO_METERS

    @classmethod
    def kilometers_to_feet(cls, kilometers):
        return kilometers * cls.KILOMETERS_TO_FEET

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.meters_to_feet(100))
    print(converter.meters_to_kilometers(1500))
    print(converter.feet_to_meters(1000))
    print(converter.feet_to_kilometers(3280.84))
    print(converter.kilometers_to_meters(5))
    print(converter.kilometers_to_feet(1))