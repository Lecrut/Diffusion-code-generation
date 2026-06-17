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
    def from_meters(self, meters, unit):
        if unit == 'm':
            return meters
        elif unit == 'km':
            return meters / 1000.0
        elif unit == 'mi':
            return meters / 1609.344
        else:
            raise ValueError("Invalid unit. Use 'm', 'km', or 'mi'.")
if __name__ == '__main__':
    converter = DistanceConverter()
    sample_value = 10
    print(f"--- Converting {sample_value} ---")
    meters_result = converter.to_meters(sample_value, 'm')
    print(f"{sample_value} meters to meters: {meters_result:.4f}")
    kilometers_result = converter.to_meters(sample_value, 'km')
    print(f"{sample_value} kilometers to meters: {kilometers_result:.4f}")
    miles_result = converter.to_meters(sample_value, 'mi')
    print(f"{sample_value} miles to meters: {miles_result:.4f}")
    print("\n--- Converting from Meters ---")
    m_to_km = converter.from_meters(10000, 'm')
    print(f"10000 meters to kilometers: {m_to_km:.4f} km")
    km_to_mi = converter.from_meters(1609344.4, 'm')
    print(f"1609344.4 meters to miles: {km_to_mi:.4f} mi")