class UnitConverter:
    METERS_TO_FEET = 3.28084
    METERS_TO_KM = 0.001
    def to_feet(self, meters):
        return meters * self.METERS_TO_FEET
    def to_kilometers(self, meters):
        return meters * self.METERS_TO_KM
    def to_meters(self, feet):
        return feet / self.METERS_TO_FEET
    def to_kilometers_from_feet(self, feet):
        return feet / self.METERS_TO_FEET * self.METERS_TO_KM
if __name__ == '__main__':
    converter = UnitConverter()
    meters_value = 10
    feet_value = 32.8084
    kilometers_value = 1000
    feet_from_meters = converter.to_feet(meters_value)
    kilometers_from_meters = converter.to_kilometers(meters_value)
    meters_from_feet = converter.to_meters(feet_value)
    kilometers_from_feet = converter.to_kilometers_from_feet(feet_value)
    print(f"10 meters is {feet_from_meters:.4f} feet")
    print(f"10 meters is {kilometers_from_meters:.4f} kilometers")
    print(f"32.8084 feet is {meters_from_feet:.4f} meters")
    print(f"32.8084 feet is {kilometers_from_feet:.4f} kilometers")