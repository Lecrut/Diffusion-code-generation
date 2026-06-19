class DistanceConverter:
    def __init__(self):
        self.meters_to_kilometers = 0.001
        self.kilometers_to_miles = 0.621371
        self.miles_to_kilometers = 1.60934

    def meters_to_kilometers(self, meters: float) -> float:
        return meters * self.meters_to_kilometers

    def kilometers_to_meters(self, kilometers: float) -> float:
        return kilometers / self.meters_to_kilometers

    def kilometers_to_miles(self, kilometers: float) -> float:
        return kilometers * self.kilometers_to_miles

    def miles_to_kilometers(self, miles: float) -> float:
        return miles / self.kilometers_to_miles

    def meters_to_miles(self, meters: float) -> float:
        kilometers = self.meters_to_kilometers(meters)
        return self.kilometers_to_miles(kilometers)

    def miles_to_meters(self, miles: float) -> float:
        kilometers = self.miles_to_kilometers(miles)
        return self.kilometers_to_meters(kilometers)

if __name__ == '__main__':
    converter = DistanceConverter()
    
    sample_meters = 1000
    sample_kilometers = 5
    sample_miles = 3

    print(f"{sample_meters} meters is {converter.meters_to_kilometers(sample_meters)} kilometers")
    print(f"{sample_kilometers} kilometers is {converter.kilometers_to_miles(sample_kilometers)} miles")
    print(f"{sample_miles} miles is {converter.miles_to_meters(sample_miles)} meters")