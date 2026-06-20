class UnitConverter:
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / 3.28084
    METERS_TO_KILOMETERS = 0.001
    KILOMETERS_TO_METERS = 1000.0

    def convert_meters_to_feet(self, meters):
        return meters * self.METERS_TO_FEET

    def convert_feet_to_meters(self, feet):
        return feet * self.FEET_TO_METERS

    def convert_meters_to_kilometers(self, meters):
        return meters * self.METERS_TO_KILOMETERS

    def convert_kilometers_to_meters(self, kilometers):
        return kilometers * self.KILOMETERS_TO_METERS

    def convert_kilometers_to_feet(self, kilometers):
        meters = self.convert_kilometers_to_meters(kilometers)
        return self.convert_meters_to_feet(meters)

    def convert_feet_to_kilometers(self, feet):
        meters = self.convert_feet_to_meters(feet)
        return self.convert_meters_to_kilometers(meters)

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.convert_meters_to_feet(100)
    print(result)
    result2 = converter.convert_kilometers_to_meters(2.5)
    print(result2)
    result3 = converter.convert_feet_to_kilometers(1000)
    print(result3)