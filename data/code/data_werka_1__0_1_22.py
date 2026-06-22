class UnitConverter:
    METERS_TO_FEET = 3.28084
    METERS_TO_KILOMETERS = 0.001
    FEET_TO_METERS = 1 / 3.28084
    KILOMETERS_TO_METERS = 1000

    def meters_to_feet(self, value):
        return value * self.METERS_TO_FEET

    def feet_to_meters(self, value):
        return value * self.FEET_TO_METERS

    def meters_to_kilometers(self, value):
        return value * self.METERS_TO_KILOMETERS

    def kilometers_to_meters(self, value):
        return value * self.KILOMETERS_TO_METERS

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.meters_to_feet(10))
    print(converter.feet_to_meters(32.8084))
    print(converter.meters_to_kilometers(5000))
    print(converter.kilometers_to_meters(2))