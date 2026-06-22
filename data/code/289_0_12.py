class DistanceConverter:
    def km_to_meters(self, kilometers):
        return kilometers * 1000

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_distance_km = 5
    meters_result = converter.km_to_meters(sample_distance_km)
    print(f"Input distance in kilometers: {sample_distance_km}")
    print(f"Converted distance in meters: {meters_result}")