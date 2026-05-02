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
    meters_from_km = converter.to_meters(5.5, 'km')
    print(f"5.5 km is {meters_from_km} meters")
    meters_from_mi = converter.to_meters(10.0, 'mi')
    print(f"10.0 mi is {meters_from_mi} meters")
    km_from_meters = converter.from_meters(2500.0, 'm')
    print(f"2500.0 m is {km_from_meters} km")
    mi_from_meters = converter.from_meters(1609344.4, 'm')
    print(f"1609344.4 m is {mi_from_meters} mi")
    km_to_mi = converter.from_meters(5000.0, 'km')
    print(f"5000.0 km is {km_to_mi} mi")