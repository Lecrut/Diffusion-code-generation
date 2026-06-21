class UnitConverter:
    METER_TO_FEET = 3.28084
    KILOMETER_TO_METER = 1000

    def meters_to_feet(self, meters):
        return meters * self.METER_TO_FEET

    def feet_to_meters(self, feet):
        return feet / self.METER_TO_FEET

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.KILOMETER_TO_METER

    def meters_to_kilometers(self, meters):
        return meters / self.KILOMETER_TO_METER

if __name__ == '__main__':
    converter = UnitConverter()
    sample_meters = 10
    sample_feet = 32.8084
    sample_kilometers = 5

    print(f"{sample_meters} meters is {converter.meters_to_feet(sample_meters)} feet")
    print(f"{sample_feet} feet is {converter.feet_to_meters(sample_feet)} meters")
    print(f"{sample_kilometers} kilometers is {converter.kilometers_to_meters(sample_kilometers)} meters")
    print(f"{sample_meters} meters is {converter.meters_to_kilometers(sample_meters)} kilometers")