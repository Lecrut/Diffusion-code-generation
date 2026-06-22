class DistanceConverter:

    def __init__(self):
        self.meters_to_kilometers = 0.001
        self.kilometers_to_miles = 0.621371
        self.miles_to_kilometers = 1.60934

    def meters_to_kilometers(self, meters: float) -> float:
        return meters * self.meters_to_kilometers

    def kilometers_to_meters(self, kilometers: float) -> float:
        return kilometers / self.meters_to_kilometers

    def meters_to_miles(self, meters: float) -> float:
        return meters * self.meters_to_kilometers * self.kilometers_to_miles

    def miles_to_meters(self, miles: float) -> float:
        return miles / self.kilometers_to_miles / self.meters_to_kilometers

    def kilometers_to_miles(self, kilometers: float) -> float:
        return kilometers * self.kilometers_to_miles

    def miles_to_kilometers(self, miles: float) -> float:
        return miles / self.kilometers_to_miles
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.meters_to_kilometers(1000))
    print(converter.kilometers_to_meters(1.0))
    print(converter.meters_to_miles(1609.34))
    print(converter.miles_to_meters(1.0))
    print(converter.kilometers_to_miles(5.0))
    print(converter.miles_to_kilometers(3.10686))