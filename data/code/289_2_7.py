class DistanceConverter:
    def __init__(self):
        self.to_meter = 1.0
        self.from_meter = 1.0
    def to_meters(self, value, unit):
        if unit == 'm':
            return value
        elif unit == 'km':
            return value * 1000.0
        elif unit == 'mi':
            return value * 1609.344
        else:
            raise ValueError("Invalid unit. Use 'm', 'km', or 'mi'.")
    def from_meters(self, value, unit):
        if unit == 'm':
            return value
        elif unit == 'km':
            return value / 1000.0
        elif unit == 'mi':
            return value / 1609.344
        else:
            raise ValueError("Invalid unit. Use 'm', 'km', or 'mi'.")
if __name__ == '__main__':
    converter = DistanceConverter()
    sample_value = 10
    meters = converter.to_meters(sample_value, 'm')
    kilometers = converter.to_meters(sample_value, 'km')
    miles = converter.to_meters(sample_value, 'mi')
    print(f"{sample_value} meters is: {meters:.2f} m")
    print(f"{sample_value} meters is: {kilometers:.2f} km")
    print(f"{sample_value} meters is: {miles:.2f} mi")
    print("-" * 20)
    test_conversion = 5.5
    meters_from_km = converter.from_meters(5500, 'km')
    print(f"5500 km converted to meters: {meters_from_km:.2f} m")
    miles_from_mi = converter.from_meters(8046.72, 'mi')
    print(f"8046.72 mi converted to meters: {miles_from_mi:.2f} m")