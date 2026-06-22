class UnitConverter:
    METERS_TO_FEET = 3.28084
    METERS_TO_KILOMETERS = 0.001

    def meters_to_feet(self, value):
        return value * self.METERS_TO_FEET

    def meters_to_kilometers(self, value):
        return value * self.METERS_TO_KILOMETERS

    def feet_to_meters(self, value):
        return value / self.METERS_TO_FEET

    def feet_to_kilometers(self, value):
        meters = self.feet_to_meters(value)
        return self.meters_to_kilometers(meters)

    def kilometers_to_meters(self, value):
        return value / self.METERS_TO_KILOMETERS

    def kilometers_to_feet(self, value):
        meters = self.kilometers_to_meters(value)
        return self.meters_to_feet(meters)

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.meters_to_feet(10))
    print(converter.feet_to_meters(32.8084))
    print(converter.kilometers_to_feet(1))