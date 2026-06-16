class DistanceConverter:
    def __init__(self):
        self.to_meter = 1.0
        self.from_meter = 1.0
    def to_meters(self, value, unit):
        if unit == 'm':
            self.from_meter = value
            self.to_meter = value
        elif unit == 'km':
            self.from_meter = value * 1000.0
            self.to_meter = value * 1000.0
        elif unit == 'mi':
            self.from_meter = value * 1609.344
            self.to_meter = value * 1609.344
        else:
            raise ValueError("Invalid unit. Use 'm', 'km', or 'mi'.")
    def from_meters(self, meters):
        if self.from_meter == 0:
            return 0.0
        if self.to_meter == 0:
            return float('inf')
        return meters / self.to_meter
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        meters = 0.0
        if from_unit == 'm':
            meters = value
        elif from_unit == 'km':
            meters = value * 1000.0
        elif from_unit == 'mi':
            meters = value * 1609.344
        else:
            raise ValueError("Invalid 'from_unit'.")
        if to_unit == 'm':
            return meters
        elif to_unit == 'km':
            return meters / 1000.0
        elif to_unit == 'mi':
            return meters / 1609.344
        else:
            raise ValueError("Invalid 'to_unit'.")
if __name__ == '__main__':
    converter = DistanceConverter()
    print("--- Conversion Tests ---")
    km_value = 5.0
    meters_from_km = converter.convert(km_value, 'km', 'm')
    print(f"{km_value} km is {meters_from_km:.2f} m")
    mi_value = 10.0
    meters_from_mi = converter.convert(mi_value, 'mi', 'm')
    print(f"{mi_value} mi is {meters_from_mi:.2f} m")
    m_value = 1500.0
    km_from_m = converter.convert(m_value, 'm', 'km')
    print(f"{m_value} m is {km_from_m:.2f} km")
    same_unit = 10.0
    result_same = converter.convert(same_unit, 'km', 'km')
    print(f"{same_unit} km is {result_same:.2f} km")
    mi_to_km = 10.0
    result_mi_to_km = converter.convert(mi_to_km, 'mi', 'km')
    print(f"{mi_to_km} mi is {result_mi_to_km:.2f} km")