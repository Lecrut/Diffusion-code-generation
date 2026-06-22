class DistanceConverter:
    @staticmethod
    def convert_km_to_miles(km):
        return km * 0.621371

    @staticmethod
    def convert_miles_to_km(miles):
        return miles / 0.621371

if __name__ == '__main__':
    distance_km = 10
    converted_miles = DistanceConverter.convert_km_to_miles(distance_km)
    print(f"{distance_km} km is {converted_miles:.2f} miles")

    distance_miles = 5
    converted_km = DistanceConverter.convert_miles_to_km(distance_miles)
    print(f"{distance_miles} miles is {converted_km:.2f} km")