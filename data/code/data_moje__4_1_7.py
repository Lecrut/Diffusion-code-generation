class DistanceConverter:
    MILES_PER_KILOMETER = 0.621371
    METERS_PER_KILOMETER = 1000
    METERS_PER_MILE = 1609.344

    def __init__(self):
        self.meters_per_mile = self.METERS_PER_MILE
        self.miles_per_kilometer = self.MILES_PER_KILOMETER
        self.meters_per_kilometer = self.METERS_PER_KILOMETER

    def meters_to_kilometers(self, meters):
        if meters < 0:
            raise ValueError("Distance cannot be negative")
        return meters / self.meters_per_kilometer

    def kilometers_to_meters(self, kilometers):
        if kilometers < 0:
            raise ValueError("Distance cannot be negative")
        return kilometers * self.meters_per_kilometer

    def meters_to_miles(self, meters):
        if meters < 0:
            raise ValueError("Distance cannot be negative")
        return meters / self.meters_per_mile

    def miles_to_meters(self, miles):
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles * self.meters_per_mile

    def kilometers_to_miles(self, kilometers):
        if kilometers < 0:
            raise ValueError("Distance cannot be negative")
        return kilometers * self.miles_per_kilometer

    def miles_to_kilometers(self, miles):
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles / self.miles_per_kilometer

if __name__ == '__main__':
    converter = DistanceConverter()
    test_meters = 1609.344
    print(converter.meters_to_kilometers(test_meters))
    print(converter.meters_to_miles(test_meters))
    print(converter.kilometers_to_miles(10))
    print(converter.miles_to_kilometers(5))