class UnitConverter:
    METERS_TO_FEET = 3.28084
    METERS_TO_KILOMETERS = 0.001
    FEET_TO_METERS = 1 / 3.28084
    KILOMETERS_TO_METERS = 1000

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

if __name__ == '__main__':
    converter = UnitConverter()
    result1 = converter.meters_to_feet(10)
    print(result1)
    result2 = converter.feet_to_meters(32.8084)
    print(result2)
    result3 = converter.meters_to_kilometers(5000)
    print(result3)
    result4 = converter.kilometers_to_meters(2)
    print(result4)