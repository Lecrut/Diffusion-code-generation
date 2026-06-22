class DistanceConverter:
    METER_TO_KM = 0.001
    METER_TO_MILE = 0.000621371
    KM_TO_METER = 1000
    KM_TO_MILE = 0.621371
    MILE_TO_METER = 1609.344
    MILE_TO_KM = 1.609344

    @staticmethod
    def meters_to_kilometers(meters):
        return meters * DistanceConverter.METER_TO_KM

    @staticmethod
    def meters_to_miles(meters):
        return meters * DistanceConverter.METER_TO_MILE

    @staticmethod
    def kilometers_to_meters(kilometers):
        return kilometers * DistanceConverter.KM_TO_METER

    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * DistanceConverter.KM_TO_MILE

    @staticmethod
    def miles_to_meters(miles):
        return miles * DistanceConverter.MILE_TO_METER

    @staticmethod
    def miles_to_kilometers(miles):
        return miles * DistanceConverter.MILE_TO_KM

if __name__ == '__main__':
    sample_meters = 1000
    sample_kilometers = 5.0
    sample_miles = 3.0
    
    km_result = DistanceConverter.meters_to_kilometers(sample_meters)
    miles_result = DistanceConverter.meters_to_miles(sample_meters)
    meters_from_km = DistanceConverter.kilometers_to_meters(sample_kilometers)
    miles_from_km = DistanceConverter.kilometers_to_miles(sample_kilometers)
    meters_from_miles = DistanceConverter.miles_to_meters(sample_miles)
    km_from_miles = DistanceConverter.miles_to_kilometers(sample_miles)

    print(f"{sample_meters} meters is {km_result} kilometers")
    print(f"{sample_meters} meters is {miles_result} miles")
    print(f"{sample_kilometers} kilometers is {meters_from_km} meters")
    print(f"{sample_kilometers} kilometers is {miles_from_km} miles")
    print(f"{sample_miles} miles is {meters_from_miles} meters")
    print(f"{sample_miles} miles is {km_from_miles} kilometers")