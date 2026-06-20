class UnitConverter:
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 0.3048
    METERS_TO_KILOMETERS = 0.001
    KILOMETERS_TO_METERS = 1000

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert_to_feet(self):
        if self.unit == 'meters':
            return self.value * UnitConverter.METERS_TO_FEET
        elif self.unit == 'kilometers':
            meters = self.value * UnitConverter.KILOMETERS_TO_METERS
            return meters * UnitConverter.METERS_TO_FEET
        elif self.unit == 'feet':
            return self.value

    def convert_to_meters(self):
        if self.unit == 'meters':
            return self.value
        elif self.unit == 'feet':
            return self.value * UnitConverter.FEET_TO_METERS
        elif self.unit == 'kilometers':
            return self.value * UnitConverter.KILOMETERS_TO_METERS

    def convert_to_kilometers(self):
        if self.unit == 'meters':
            return self.value * UnitConverter.METERS_TO_KILOMETERS
        elif self.unit == 'feet':
            meters = self.value * UnitConverter.FEET_TO_METERS
            return meters * UnitConverter.METERS_TO_KILOMETERS
        elif self.unit == 'kilometers':
            return self.value

if __name__ == '__main__':
    converter_meters = UnitConverter(100, 'meters')
    print(converter_meters.convert_to_feet())
    print(converter_meters.convert_to_kilometers())
    
    converter_kilometers = UnitConverter(5, 'kilometers')
    print(converter_kilometers.convert_to_meters())
    print(converter_kilometers.convert_to_feet())
    
    converter_feet = UnitConverter(10, 'feet')
    print(converter_feet.convert_to_meters())
    print(converter_feet.convert_to_kilometers())