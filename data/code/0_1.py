class UnitConverter:
    METER_TO_FOOT = 3.28084
    METER_TO_KILOMETER = 0.001
    FOOT_TO_METER = 1 / METER_TO_FOOT
    KILOMETER_TO_METER = 1000.0

    @classmethod
    def meters_to_feet(cls, value):
        return value * cls.METER_TO_FOOT

    @classmethod
    def meters_to_kilometers(cls, value):
        return value * cls.METER_TO_KILOMETER

    @classmethod
    def feet_to_meters(cls, value):
        return value * cls.FOOT_TO_METER

    @classmethod
    def kilometers_to_meters(cls, value):
        return value * cls.KILOMETER_TO_METER

    @classmethod
    def feet_to_kilometers(cls, value):
        meters = cls.feet_to_meters(value)
        return cls.meters_to_kilometers(meters)

    @classmethod
    def kilometers_to_feet(cls, value):
        meters = cls.kilometers_to_meters(value)
        return cls.meters_to_feet(meters)

if __name__ == '__main__':
    result = UnitConverter.meters_to_feet(10)
    print(result)
    
    result2 = UnitConverter.kilometers_to_meters(5)
    print(result2)
    
    result3 = UnitConverter.feet_to_kilometers(1000)
    print(result3)