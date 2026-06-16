class DistanceConverter:
    def to_miles(self, distance, unit):
        if unit.lower() == 'miles':
            return distance
        elif unit.lower() == 'kilometers':
            return distance / 1.60934
        elif unit.lower() == 'meters':
            return distance / 1609.34
        else:
            raise ValueError("Unsupported unit")
    def to_kilometers(self, distance, unit):
        if unit.lower() == 'kilometers':
            return distance
        elif unit.lower() == 'miles':
            return distance * 1.60934
        elif unit.lower() == 'meters':
            return distance / 1000.0
        else:
            raise ValueError("Unsupported unit")
    def to_meters(self, distance, unit):
        if unit.lower() == 'meters':
            return distance
        elif unit.lower() == 'kilometers':
            return distance * 1000.0
        elif unit.lower() == 'miles':
            return distance * 1609.34
        else:
            raise ValueError("Unsupported unit")
if __name__ == '__main__':
    converter = DistanceConverter()
    sample_distance = 10
    print(f"Converting {sample_distance} miles to kilometers:")
    km = converter.to_kilometers(sample_distance, 'miles')
    print(f"{sample_distance} miles is equal to {km:.2f} kilometers")
    print(f"\nConverting 5 kilometers to meters:")
    meters = converter.to_meters(5, 'kilometers')
    print(f"5 kilometers is equal to {meters:.2f} meters")
    print(f"\nConverting 1000 meters to miles:")
    miles = converter.to_miles(1000, 'meters')
    print(f"1000 meters is equal to {miles:.2f} miles")