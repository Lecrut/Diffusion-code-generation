class DistanceConverter:
    UNITS = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }

    def __init__(self):
        self.supported_units = list(self.UNITS.keys())

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in self.supported_units:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.supported_units:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        meters = value * self.UNITS[from_unit]
        result = meters / self.UNITS[to_unit]
        return result

if __name__ == '__main__':
    converter = DistanceConverter()
    result_m_to_km = converter.convert(1500, 'm', 'km')
    print(result_m_to_km)
    result_miles_to_meters = converter.convert(5, 'mi', 'm')
    print(result_miles_to_meters)
    result_cm_to_in = converter.convert(30, 'cm', 'in')
    print(result_cm_to_in)