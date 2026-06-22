class UnitConverter:
    METER_TO_FOOT = 3.28084
    FOOT_TO_METER = 0.3048
    METER_TO_KILOMETER = 0.001
    KILOMETER_TO_METER = 1000

    def meters_to_feet(self, meters):
        return meters * UnitConverter.METER_TO_FOOT

    def feet_to_meters(self, feet):
        return feet * UnitConverter.FOOT_TO_METER

    def meters_to_kilometers(self, meters):
        return meters * UnitConverter.METER_TO_KILOMETER

    def kilometers_to_meters(self, kilometers):
        return kilometers * UnitConverter.KILOMETER_TO_METER

    def feet_to_kilometers(self, feet):
        meters = self.feet_to_meters(feet)
        return self.meters_to_kilometers(meters)

    def kilometers_to_feet(self, kilometers):
        meters = self.kilometers_to_meters(kilometers)
        return self.meters_to_feet(meters)

if __name__ == '__main__':
    converter = UnitConverter()
    sample_meters = 100
    sample_feet = 328.084
    sample_kilometers = 1.5
    print(converter.meters_to_feet(sample_meters))
    print(converter.feet_to_meters(sample_feet))
    print(converter.meters_to_kilometers(sample_meters))
    print(converter.kilometers_to_meters(sample_kilometers))
    print(converter.feet_to_kilometers(sample_feet))
    print(converter.kilometers_to_feet(sample_kilometers))