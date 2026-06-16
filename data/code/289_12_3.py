class DistanceConverter:
    def to_miles(self, distance, unit):
        if unit.lower() == 'miles':
            return distance
        elif unit.lower() == 'km':
            return distance * 0.621371
        elif unit.lower() == 'm':
            return distance / 1609.34
        else:
            raise ValueError("Unsupported unit")
    def to_kilometers(self, distance, unit):
        if unit.lower() == 'kilometers':
            return distance
        elif unit.lower() == 'miles':
            return distance * 1.60934
        elif unit.lower() == 'm':
            return distance / 1000
        else:
            raise ValueError("Unsupported unit")
    def to_meters(self, distance, unit):
        if unit.lower() == 'meters':
            return distance
        elif unit.lower() == 'km':
            return distance * 1000
        elif unit.lower() == 'miles':
            return distance * 1609.34
        else:
            raise ValueError("Unsupported unit")
if __name__ == '__main__':
    converter = DistanceConverter()
    distance_km = 10
    miles_from_km = converter.to_miles(distance_km, 'km')
    print(f"{distance_km} km is equal to {miles_from_km:.2f} miles")
    distance_mi = 5
    km_from_mi = converter.to_kilometers(distance_mi, 'miles')
    print(f"{distance_mi} miles is equal to {km_from_mi:.2f} km")
    distance_m = 100
    meters_from_km = converter.to_meters(distance_km, 'km')
    print(f"{distance_km} km is equal to {meters_from_km:.2f} meters")
    meters_from_mi = converter.to_meters(distance_mi, 'miles')
    print(f"{distance_mi} miles is equal to {meters_from_mi:.2f} meters")