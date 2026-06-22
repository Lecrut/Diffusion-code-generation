class DistanceConverter:
    KILOMETERS_TO_MILES = 0.621371
    MILES_TO_KILOMETERS = 1.60934

    @staticmethod
    def meters_to_kilometers(meters):
        return meters / 1000.0

    @staticmethod
    def meters_to_miles(meters):
        return meters / 1000.0 * DistanceConverter.KILOMETERS_TO_MILES

    @staticmethod
    def kilometers_to_meters(kilometers):
        return kilometers * 1000.0

    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * DistanceConverter.KILOMETERS_TO_MILES

    @staticmethod
    def miles_to_meters(miles):
        return miles * DistanceConverter.MILES_TO_KILOMETERS * 1000.0

    @staticmethod
    def miles_to_kilometers(miles):
        return miles * DistanceConverter.MILES_TO_KILOMETERS

if __name__ == '__main__':
    sample_meters = 5000.0
    sample_kilometers = 10.0
    sample_miles = 2.5
    
    km_from_meters = DistanceConverter.meters_to_kilometers(sample_meters)
    miles_from_meters = DistanceConverter.meters_to_miles(sample_meters)
    meters_from_km = DistanceConverter.kilometers_to_meters(sample_kilometers)
    miles_from_km = DistanceConverter.kilometers_to_miles(sample_kilometers)
    meters_from_miles = DistanceConverter.miles_to_meters(sample_miles)
    km_from_miles = DistanceConverter.miles_to_kilometers(sample_miles)

    print(km_from_meters)
    print(miles_from_meters)
    print(meters_from_km)
    print(miles_from_km)
    print(meters_from_miles)
    print(km_from_miles)