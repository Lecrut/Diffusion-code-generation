class UnitConverter:
    METERS_TO_FEET = 3.28084
    METERS_TO_KILOMETERS = 0.001
    FEET_TO_METERS = 1 / 3.28084
    KILOMETERS_TO_METERS = 1000.0

    def meters_to_feet(self, meters):
        return meters * self.METERS_TO_FEET

    def meters_to_kilometers(self, meters):
        return meters * self.METERS_TO_KILOMETERS

    def feet_to_meters(self, feet):
        return feet * self.FEET_TO_METERS

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.KILOMETERS_TO_METERS

    def feet_to_kilometers(self, feet):
        return self.feet_to_meters(feet) * self.METERS_TO_KILOMETERS

    def kilometers_to_feet(self, kilometers):
        return self.kilometers_to_meters(kilometers) * self.METERS_TO_FEET

if __name__ == '__main__':
    converter = UnitConverter()

    meters = 100.0
    feet = 328.084
    kilometers = 1.0

    print(f"{meters} meters is {converter.meters_to_feet(meters)} feet")
    print(f"{meters} meters is {converter.meters_to_kilometers(meters)} kilometers")
    print(f"{feet} feet is {converter.feet_to_meters(feet)} meters")
    print(f"{kilometers} kilometers is {converter.kilometers_to_meters(kilometers)} meters")
    print(f"{feet} feet is {converter.feet_to_kilometers(feet)} kilometers")
    print(f"{kilometers} kilometers is {converter.kilometers_to_feet(kilometers)} feet")