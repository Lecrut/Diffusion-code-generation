class DistanceConverter:
    def convert_to_miles(self, kilometers):
        return kilometers * 0.621371

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_km = 100.5
    result_miles = converter.convert_to_miles(sample_km)
    print(f"Original distance: {sample_km:.2f} kilometers")
    print(f"Converted distance: {result_miles:.2f} miles")