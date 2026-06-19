class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_METERS = 1000
    MILES_TO_METERS = MILES_TO_KILOMETERS * KILOMETERS_TO_METERS

    def miles_to_kilometers(self, miles):
        return miles * self.MILES_TO_KILOMETERS

    def kilometers_to_miles(self, kilometers):
        return kilometers / self.MILES_TO_KILOMETERS

    def meters_to_kilometers(self, meters):
        return meters / self.KILOMETERS_TO_METERS

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.KILOMETERS_TO_METERS

    def miles_to_meters(self, miles):
        return miles * self.MILES_TO_METERS

    def meters_to_miles(self, meters):
        return meters / self.MILES_TO_METERS
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.miles_to_kilometers(10))
    print(converter.kilometers_to_meters(5))
    print(converter.miles_to_meters(2))