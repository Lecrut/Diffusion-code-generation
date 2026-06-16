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
    meters_value = 500
    print(f"{meters_value} meters to km: {converter.to_meters(meters_value, 'km'):.4f}")
    print(f"{meters_value} meters to miles: {converter.to_meters(meters_value, 'mi'):.4f}")
    km_value = 10
    print(f"{km_value} kilometers to meters: {converter.from_meters(km_value, 'm'):.2f}")
    print(f"{km_value} kilometers to miles: {converter.from_meters(km_value, 'mi'):.4f}")
    miles_value = 10
    print(f"{miles_value} miles to meters: {converter.from_meters(miles_value, 'm'):.2f}")
    print(f"{miles_value} miles to kilometers: {converter.from_meters(miles_value, 'km'):.4f}")