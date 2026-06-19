class DistanceConverter:
    def __init__(self):
        self.meters_to_kilometers = 0.001
        self.meters_to_miles = 0.000621371

    def meters_to_kilometers(self, meters):
        return meters * self.meters_to_kilometers

    def meters_to_miles(self, meters):
        return meters * self.meters_to_miles

    def kilometers_to_meters(self, kilometers):
        return kilometers / self.meters_to_kilometers

    def kilometers_to_miles(self, kilometers):
        return kilometers / self.meters_to_kilometers / self.meters_to_miles

    def miles_to_meters(self, miles):
        return miles / self.meters_to_miles

    def miles_to_kilometers(self, miles):
        return miles / self.meters_to_miles / self.meters_to_kilometers

if __name__ == '__main__':
    converter = DistanceConverter()
    
    sample_meters = 1000
    print(f"{sample_meters} meters is {converter.meters_to_kilometers(sample_meters)} kilometers")
    print(f"{sample_meters} meters is {converter.meters_to_miles(sample_meters)} miles")

    sample_kilometers = 5
    print(f"{sample_kilometers} kilometers is {converter.kilometers_to_meters(sample_kilometers)} meters")
    print(f"{sample_kilometers} kilometers is {converter.kilometers_to_miles(sample_kilometers)} miles")

    sample_miles = 3
    print(f"{sample_miles} miles is {converter.miles_to_meters(sample_miles)} meters")
    print(f"{sample_miles} miles is {converter.miles_to_kilometers(sample_miles)} kilometers")