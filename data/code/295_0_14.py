class DistanceConverter:
    def meters_to_kilometers(self, meters):
        return round(meters / 1000.0, 2)

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_meters = 5000
    kilometers = converter.meters_to_kilometers(sample_meters)
    print(f"{sample_meters} meters is equal to {kilometers} kilometers")