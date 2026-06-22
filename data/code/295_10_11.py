class DistanceConverter:
    KM_TO_MILE_FACTOR = 0.621371

    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * DistanceConverter.KM_TO_MILE_FACTOR

if __name__ == '__main__':
    sample_km = 10.0
    miles = DistanceConverter.kilometers_to_miles(sample_km)
    print(miles)