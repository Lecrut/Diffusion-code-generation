class DistanceConverter:
    def __init__(self):
        self.factor = 0.621371

    def km_to_miles(self, kilometers):
        return kilometers * self.factor

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_km = 100
    result_miles = converter.km_to_miles(sample_km)
    print(f"{sample_km} kilometers is equal to {result_miles:.2f} miles.")