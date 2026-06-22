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
    
    sample_miles = 5
    sample_kilometers = 10
    sample_meters = 1000
    
    print(f"{sample_miles} miles is {converter.miles_to_kilometers(sample_miles)} kilometers")
    print(f"{sample_kilometers} kilometers is {converter.kilometers_to_miles(sample_kilometers)} miles")
    print(f"{sample_meters} meters is {converter.meters_to_kilometers(sample_meters)} kilometers")
    print(f"{sample_kilometers} kilometers is {converter.kilometers_to_meters(sample_kilometers)} meters")
    print(f"{sample_miles} miles is {converter.miles_to_meters(sample_miles)} meters")
    print(f"{sample_meters} meters is {converter.meters_to_miles(sample_meters)} miles")