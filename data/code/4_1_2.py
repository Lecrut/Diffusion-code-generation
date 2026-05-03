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
    meters_to_km = converter.to_meters(5000, 'm')
    print(f"5000 meters is {meters_to_km:.3f} kilometers")
    meters_to_mi = converter.to_meters(10000, 'm')
    print(f"10000 meters is {meters_to_mi:.3f} miles")
    km_to_m = converter.from_meters(2.5, 'km')
    print(f"2.5 kilometers is {km_to_m:.3f} meters")
    mi_to_m = converter.from_meters(10, 'mi')
    print(f"10 miles is {mi_to_m:.3f} meters")
    km_to_mi = converter.from_meters(1000, 'km')
    print(f"1000 kilometers is {km_to_mi:.3f} miles")