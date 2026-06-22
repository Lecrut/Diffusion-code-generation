class DistanceConverter:
    def km_to_miles(self, kilometers):
        return kilometers * 0.621371

if __name__ == '__main__':
    converter = DistanceConverter()
    distance_km = 10.0
    distance_mi = converter.km_to_miles(distance_km)
    print(f"{distance_km} km is equal to {distance_mi:.2f} miles")