class UnitConverter:
    METERS_TO_FEET = 3.28084
    METERS_TO_KILOMETERS = 0.001

    @classmethod
    def meters_to_feet(cls, meters):
        return meters * cls.METERS_TO_FEET

    @classmethod
    def feet_to_meters(cls, feet):
        return feet / cls.METERS_TO_FEET

    @classmethod
    def meters_to_kilometers(cls, meters):
        return meters * cls.METERS_TO_KILOMETERS

    @classmethod
    def kilometers_to_meters(cls, kilometers):
        return kilometers / cls.METERS_TO_KILOMETERS

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
    
    result1 = converter.meters_to_feet(10)
    print(f"10 meters is {result1} feet")
    
    result2 = converter.kilometers_to_meters(5)
    print(f"5 kilometers is {result2} meters")
    
    result3 = converter.feet_to_kilometers(1000)
    print(f"1000 feet is {result3} kilometers")