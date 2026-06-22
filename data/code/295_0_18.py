class DistanceConverter:
    def meters_to_kilometers(self, meters):
        return meters / 1000.0

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_meters = 5000.0
    kilometers = converter.meters_to_kilometers(sample_meters)
    print(f"{sample_meters} meters is equal to {kilometers:.2f} kilometers")