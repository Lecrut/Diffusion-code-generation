class UnitConverter:
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / METERS_TO_FEET
    METERS_TO_KILOMETERS = 1 / 1000
    KILOMETERS_TO_METERS = 1000
    def meters_to_feet(self, meters):
        return meters * self.METERS_TO_FEET
    def feet_to_meters(self, feet):
        return feet * self.FEET_TO_METERS
    def meters_to_kilometers(self, meters):
        return meters * self.METERS_TO_KILOMETERS
    def kilometers_to_meters(self, kilometers):
        return kilometers * self.KILOMETERS_TO_METERS
if __name__ == '__main__':
    converter = UnitConverter()
    meters_value = 10
    feet_value = 32.8084
    kilometers_value = 5
    meters_to_feet_result = converter.meters_to_feet(meters_value)
    feet_to_meters_result = converter.feet_to_meters(feet_value)
    meters_to_kilometers_result = converter.meters_to_kilometers(meters_value)
    kilometers_to_meters_result = converter.kilometers_to_meters(kilometers_value)
    print(f"10 meters is equal to {meters_to_feet_result:.4f} feet")
    print(f"{feet_value} feet is equal to {feet_to_meters_result:.4f} meters")
    print(f"10 meters is equal to {meters_to_kilometers_result:.4f} kilometers")
    print(f"5 kilometers is equal to {kilometers_to_meters_result:.4f} meters")