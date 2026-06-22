class DistanceConverter:
    def km_to_m(self, kilometers):
        return kilometers * 1000

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_distance_km = 50
    result_m = converter.km_to_m(sample_distance_km)
    print(f"Input distance in kilometers: {sample_distance_km}")
    print(f"Converted distance in meters: {result_m}")