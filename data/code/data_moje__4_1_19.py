class DistanceConverter:
    MILES_PER_KILOMETER = 0.621371
    METERS_PER_KILOMETER = 1000.0
    METERS_PER_MILE = 1609.34

    @staticmethod
    def meters_to_kilometers(meters):
        return meters / DistanceConverter.METERS_PER_KILOMETER

    @staticmethod
    def kilometers_to_meters(kilometers):
        return kilometers * DistanceConverter.METERS_PER_KILOMETER

    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * DistanceConverter.MILES_PER_KILOMETER

    @staticmethod
    def miles_to_kilometers(miles):
        return miles / DistanceConverter.MILES_PER_KILOMETER

    @staticmethod
    def meters_to_miles(meters):
        return meters / DistanceConverter.METERS_PER_MILE

    @staticmethod
    def miles_to_meters(miles):
        return miles * DistanceConverter.METERS_PER_MILE

if __name__ == '__main__':
    initial_meters = 1609.34
    initial_kilometers = 10.0
    initial_miles = 5.0

    km_result = DistanceConverter.meters_to_kilometers(initial_meters)
    miles_result = DistanceConverter.kilometers_to_miles(initial_kilometers)
    km_from_miles = DistanceConverter.miles_to_kilometers(initial_miles)
    meters_from_miles = DistanceConverter.miles_to_meters(initial_miles)

    print(f"{initial_meters} meters is {km_result} kilometers")
    print(f"{initial_kilometers} kilometers is {miles_result} miles")
    print(f"{initial_miles} miles is {km_from_miles} kilometers")
    print(f"{initial_miles} miles is {meters_from_miles} meters")