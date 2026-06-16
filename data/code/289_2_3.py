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
    meters_value = 1000.0
    print(f"{meters_value} meters is equal to {converter.to_meters(meters_value, 'm'):.2f} meters")
    print(f"{meters_value} meters is equal to {converter.to_meters(meters_value, 'km'):.2f} kilometers")
    print(f"{meters_value} meters is equal to {converter.to_meters(meters_value, 'mi'):.2f} miles")
    print("-" * 20)
    km_value = 5.5
    print(f"{km_value} kilometers is equal to {converter.from_meters(5500.0, 'km'):.2f} meters")
    print(f"{km_value} kilometers is equal to {converter.from_meters(8807.0, 'mi'):.2f} meters")