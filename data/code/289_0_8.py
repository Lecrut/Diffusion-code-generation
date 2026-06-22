class DistanceConverter:
    def km_to_meters(self, kilometers):
        meters = kilometers * 1000
        return meters

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_distance_km = 5.5
    result_meters = converter.km_to_meters(sample_distance_km)
    print(f"Input distance in kilometers: {sample_distance_km}")
    print(f"Converted distance in meters: {result_meters}")