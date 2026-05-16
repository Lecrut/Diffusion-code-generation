class DistanceConverter:
    def __init__(self):
        self.to_meter = 1.0
        self.from_meter = 1.0
    def convert_to_meter(self, value: float, unit: str) -> float:
        if unit.lower() == 'm':
            return value
        elif unit.lower() == 'meter':
            return value
        elif unit.lower() == 'meters':
            return value
        elif unit.lower() == 'km':
            return value * 1000.0
        elif unit.lower() == 'kilometer':
            return value * 1000.0
        elif unit.lower() == 'kilometers':
            return value * 1000.0
        elif unit.lower() == 'mi':
            return value * 1609.344
        elif unit.lower() == 'mile':
            return value * 1609.344
        else:
            raise ValueError(f"Unsupported unit: {unit}")
    def convert_from_meter(self, value: float, unit: str) -> float:
        if unit.lower() == 'm':
            return value
        elif unit.lower() == 'meter':
            return value
        elif unit.lower() == 'meters':
            return value
        elif unit.lower() == 'km':
            return value / 1000.0
        elif unit.lower() == 'kilometer':
            return value / 1000.0
        elif unit.lower() == 'kilometers':
            return value / 1000.0
        elif unit.lower() == 'mi':
            return value / 1609.344
        elif unit.lower() == 'mile':
            return value / 1609.344
        else:
            raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    converter = DistanceConverter()
    km_value = 2.5
    meters_from_km = converter.convert_to_meter(km_value, 'km')
    print(f"{km_value} km is equal to {meters_from_km} meters")
    miles_value = 10.0
    meters_from_mi = converter.convert_to_meter(miles_value, 'mi')
    print(f"{miles_value} mi is equal to {meters_from_mi} meters")
    meters_value = 5000.0
    km_from_meters = converter.convert_from_meter(meters_value, 'm')
    print(f"{meters_value} meters is equal to {km_from_meters} km")
    km_to_mi = 10.0
    miles_from_km = converter.convert_from_meter(km_to_mi * 1000.0, 'km')
    print(f"{km_to_mi} km is equal to {miles_from_km} mi")
    try:
        converter.convert_to_meter(5.0, 'furlongs')
    except ValueError as e:
        print(f"Error caught: {e}")