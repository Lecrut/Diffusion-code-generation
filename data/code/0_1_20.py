class UnitConverter:
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / 3.28084
    METERS_TO_KILOMETERS = 0.001
    KILOMETERS_TO_METERS = 1000

    @classmethod
    def convert_meters_to_feet(cls, value):
        return value * cls.METERS_TO_FEET

    @classmethod
    def convert_feet_to_meters(cls, value):
        return value * cls.FEET_TO_METERS

    @classmethod
    def convert_meters_to_kilometers(cls, value):
        return value * cls.METERS_TO_KILOMETERS

    @classmethod
    def convert_kilometers_to_meters(cls, value):
        return value * cls.KILOMETERS_TO_METERS

    @classmethod
    def convert_feet_to_kilometers(cls, value):
        return cls.convert_meters_to_kilometers(cls.convert_feet_to_meters(value))

    @classmethod
    def convert_kilometers_to_feet(cls, value):
        return cls.convert_meters_to_feet(cls.convert_kilometers_to_meters(value))

if __name__ == '__main__':
    converter = UnitConverter()
    
    meters_input = 100.0
    feet_result = converter.convert_meters_to_feet(meters_input)
    print(f"Convert {meters_input} meters to feet: {feet_result}")
    
    feet_input = 328.084
    meters_from_feet = converter.convert_feet_to_meters(feet_input)
    print(f"Convert {feet_input} feet to meters: {meters_from_feet}")
    
    meters_to_km = converter.convert_meters_to_kilometers(meters_input)
    print(f"Convert {meters_input} meters to kilometers: {meters_to_km}")
    
    km_to_meters = converter.convert_kilometers_to_meters(5.0)
    print(f"Convert 5.0 kilometers to meters: {km_to_meters}")
    
    feet_to_km = converter.convert_feet_to_kilometers(328.084)
    print(f"Convert {feet_input} feet to kilometers: {feet_to_km}")
    
    km_to_feet = converter.convert_kilometers_to_feet(1.0)
    print(f"Convert 1.0 kilometers to feet: {km_to_feet}")