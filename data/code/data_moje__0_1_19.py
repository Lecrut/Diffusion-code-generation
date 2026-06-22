class UnitConverter:
    METERS_PER_FOOT = 0.3048
    METERS_PER_KILOMETER = 1000

    def meters_to_feet(self, meters):
        return meters / self.METERS_PER_FOOT

    def feet_to_meters(self, feet):
        return feet * self.METERS_PER_FOOT

    def meters_to_kilometers(self, meters):
        return meters / self.METERS_PER_KILOMETER

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.METERS_PER_KILOMETER

    def feet_to_kilometers(self, feet):
        meters = self.feet_to_meters(feet)
        return self.meters_to_kilometers(meters)

    def kilometers_to_feet(self, kilometers):
        meters = self.kilometers_to_meters(kilometers)
        return self.meters_to_feet(meters)

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.meters_to_feet(10))
    print(converter.feet_to_meters(10))
    print(converter.meters_to_kilometers(1500))
    print(converter.kilometers_to_meters(2.5))
    print(converter.feet_to_kilometers(3280.84))
    print(converter.kilometers_to_feet(1))