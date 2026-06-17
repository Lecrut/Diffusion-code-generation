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
            self.from_meter = value * 1609.34
            self.to_meter = value * 1609.34
        else:
            raise ValueError("Invalid unit. Use 'm', 'km', or 'mi'.")
    def from_meters(self, meters):
        if self.from_meter == 0:
            return 0.0
        if self.to_meter == 0:
            raise ZeroDivisionError("Cannot convert from zero base.")
        result = meters / self.from_meter
        return result
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        meters = 0.0
        if from_unit == 'm':
            meters = value
        elif from_unit == 'km':
            meters = value * 1000.0
        elif from_unit == 'mi':
            meters = value * 1609.34
        else:
            raise ValueError("Invalid source unit.")
        if to_unit == 'm':
            return meters
        elif to_unit == 'km':
            return meters / 1000.0
        elif to_unit == 'mi':
            return meters / 1609.34
        else:
            raise ValueError("Invalid target unit.")
if __name__ == '__main__':
    converter = DistanceConverter()
    print("--- Conversion Examples ---")
    km_value = 5.5
    meters_result = converter.convert(km_value, 'km', 'm')
    print(f"{km_value} km is equal to {meters_result:.2f} m")
    mi_value = 10.0
    km_result = converter.convert(mi_value, 'mi', 'km')
    print(f"{mi_value} mi is equal to {km_result:.2f} km")
    m_value = 1000.0
    mi_result = converter.convert(m_value, 'm', 'mi')
    print(f"{m_value} m is equal to {mi_result:.2f} mi")
    same_unit = 10
    result_same = converter.convert(same_unit, 'km', 'km')
    print(f"{same_unit} km is equal to {result_same:.2f} km")