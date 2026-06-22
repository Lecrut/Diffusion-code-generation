class UnitConverter:
    METERS_TO_FEET = 3.28084
    METERS_TO_KILOMETERS = 0.001
    FEET_TO_METERS = 1 / 3.28084
    KILOMETERS_TO_METERS = 1000.0
    FEET_TO_KILOMETERS = FEET_TO_METERS / 1000.0
    KILOMETERS_TO_FEET = KILOMETERS_TO_METERS * FEET_TO_METERS

    def meters_to_feet(self, meters):
        return meters * self.METERS_TO_FEET

    def meters_to_kilometers(self, meters):
        return meters * self.METERS_TO_KILOMETERS

    def feet_to_meters(self, feet):
        return feet * self.FEET_TO_METERS

    def feet_to_kilometers(self, feet):
        return feet * self.FEET_TO_KILOMETERS

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.KILOMETERS_TO_METERS

    def kilometers_to_feet(self, kilometers):
        return kilometers * self.KILOMETERS_TO_FEET

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.meters_to_feet(10)
    print(result)