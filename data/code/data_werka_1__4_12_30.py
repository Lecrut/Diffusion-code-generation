class DistanceConverter:
    MILES_TO_KM = 1.60934
    KM_TO_M = 1000
    MILES_TO_M = MILES_TO_KM * KM_TO_M

    def miles_to_kilometers(self, miles):
        return miles * self.MILES_TO_KM

    def kilometers_to_miles(self, kilometers):
        return kilometers / self.MILES_TO_KM

    def meters_to_kilometers(self, meters):
        return meters / self.KM_TO_M

    def kilometers_to_meters(self, kilometers):
        return kilometers * self.KM_TO_M

    def miles_to_meters(self, miles):
        return miles * self.MILES_TO_M

    def meters_to_miles(self, meters):
        return meters / self.MILES_TO_M
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.miles_to_kilometers(5))
    print(converter.kilometers_to_miles(10))
    print(converter.meters_to_kilometers(1000))
    print(converter.kilometers_to_meters(5))
    print(converter.miles_to_meters(2))
    print(converter.meters_to_miles(1609.34))