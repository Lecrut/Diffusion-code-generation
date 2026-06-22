class DistanceConverter:

    def __init__(self):
        self.meters_to_kilometers_factor = 0.001
        self.meters_to_miles_factor = 0.000621371

    def meters_to_kilometers(self, meters):
        return meters * self.meters_to_kilometers_factor

    def meters_to_miles(self, meters):
        return meters * self.meters_to_miles_factor

    def kilometers_to_meters(self, kilometers):
        return kilometers / self.meters_to_kilometers_factor

    def kilometers_to_miles(self, kilometers):
        return kilometers / self.meters_to_kilometers_factor / self.meters_to_miles_factor

    def miles_to_meters(self, miles):
        return miles / self.meters_to_miles_factor

    def miles_to_kilometers(self, miles):
        return miles / self.meters_to_miles_factor / self.meters_to_kilometers_factor
if __name__ == '__main__':
    converter = DistanceConverter()
    meters_value = 1000
    kilometers_value = 5
    miles_value = 2
    print(f'{meters_value} meters is {converter.meters_to_kilometers(meters_value)} kilometers')
    print(f'{meters_value} meters is {converter.meters_to_miles(meters_value)} miles')
    print(f'{kilometers_value} kilometers is {converter.kilometers_to_meters(kilometers_value)} meters')
    print(f'{kilometers_value} kilometers is {converter.kilometers_to_miles(kilometers_value)} miles')
    print(f'{miles_value} miles is {converter.miles_to_meters(miles_value)} meters')
    print(f'{miles_value} miles is {converter.miles_to_kilometers(miles_value)} kilometers')