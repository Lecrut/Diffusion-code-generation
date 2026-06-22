class DistanceConverter:
    def __init__(self):
        self.conversion_factor = 0.621371

    def kilometers_to_miles(self, kilometers: float) -> float:
        return kilometers * self.conversion_factor

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_km = 10.0
    miles = converter.kilometers_to_miles(sample_km)
    print(f"{sample_km} kilometers is equal to {miles} miles.")